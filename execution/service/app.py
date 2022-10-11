import logging
import os
import sys

from binance.exceptions import BinanceAPIException
from flask import Flask, jsonify, request
from flask_cors import CORS

from execution.exchanges.binance.futures import BinanceFuturesTrader
from execution.exchanges.binance.margin import BinanceMarginTrader
from execution.exchanges.binance.margin.mock import BinanceMockMarginTrader
from execution.service.blueprints.market_data import market_data
from execution.service.helpers import validate_input, extract_and_validate
from execution.service.helpers.responses import Responses
from shared.utils.logger import configure_logger

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

configure_logger(os.getenv("LOGGER_LEVEL", "INFO"))

binance_futures_trader = BinanceFuturesTrader()
binance_futures_mock_trader = BinanceFuturesTrader(paper_trading=True)
binance_margin_trader = BinanceMarginTrader()
binance_margin_mock_trader = BinanceMockMarginTrader()


app = Flask(__name__)
app.register_blueprint(market_data)

CORS(app)


def get_binance_trader_instance(binance_account_type, paper_trading):

    if binance_account_type == 'futures':
        if paper_trading:
            return binance_futures_mock_trader
        else:
            return binance_futures_trader

    if binance_account_type == 'margin':
        if paper_trading:
            return binance_margin_mock_trader
        else:
            return binance_margin_trader

    return binance_futures_mock_trader


@app.route('/')
def hello_world():
    return "I'm up!"


@app.route('/start_symbol_trading', methods=['POST'])
def start_symbol_trading():

    pipeline, parameters = extract_and_validate()

    if parameters.response is not None:
        logging.debug(parameters.response)
        return parameters.response

    if parameters.equity is None:
        return jsonify(Responses.EQUITY_REQUIRED(pipeline.symbol))

    if pipeline.exchange == 'binance':

        bt = get_binance_trader_instance(parameters.binance_account_type, pipeline.paper_trading)

        success = bt.start_symbol_trading(
            pipeline.symbol,
            equity=parameters.equity,
            header=parameters.header,
            pipeline_id=pipeline.id
        )

        if success:
            return jsonify(Responses.TRADING_SYMBOL_START(pipeline.symbol))
        else:
            return jsonify(Responses.TRADING_SYMBOL_NO_ACCOUNT(pipeline.symbol))


@app.route('/stop_symbol_trading', methods=['POST'])
def stop_symbol_trading():
    pipeline, parameters = extract_and_validate()

    if parameters.response is not None:
        logging.debug(parameters.response)
        return parameters.response

    if pipeline.exchange == 'binance':

        bt = get_binance_trader_instance(parameters.binance_account_type, pipeline.paper_trading)

        success = bt.stop_symbol_trading(pipeline.symbol, header=parameters.header, pipeline_id=pipeline.id)

        if success:
            return jsonify(Responses.TRADING_SYMBOL_STOP(pipeline.symbol))
        else:
            return jsonify(Responses.TRADING_SYMBOL_NO_ACCOUNT(pipeline.symbol))


@app.route('/execute_order', methods=['POST'])
def execute_order():

    request_data = request.get_json(force=True)

    logging.debug(request_data)

    pipeline, parameters = extract_and_validate()

    if parameters.response is not None:
        logging.debug(parameters.response)
        return parameters.response

    signal = request_data.get("signal", None)
    amount = request_data.get("amount", "all")

    response = validate_input(signal=signal)

    if response is not None:
        logging.debug(response)
        return response

    if pipeline.exchange.lower() == 'binance':

        bt = get_binance_trader_instance(parameters.binance_account_type, pipeline.paper_trading)

        try:
            bt.trade(pipeline.symbol, signal, amount=amount, header=parameters.header, pipeline_id=pipeline.id)
        except BinanceAPIException as e:
            bt.stop_symbol_trading(pipeline.symbol, header=parameters.header, pipeline_id=pipeline.id)
            message = e.message
            return jsonify(Responses.API_ERROR(pipeline.symbol, message))

        return jsonify(Responses.ORDER_EXECUTION_SUCCESS(pipeline.symbol))


if __name__ == "__main__":
    app.run(host='0.0.0.0')

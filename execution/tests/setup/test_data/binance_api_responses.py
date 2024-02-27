from random import randint

isolated_account_info = {
    "assets": [
        {
            "baseAsset": {
                "asset": "BTC",
                "borrowEnabled": True,
                "borrowed": "10.00000000",
                "free": "10.00000000",
                "interest": "0.00000000",
                "locked": "0.00000000",
                "netAsset": "0.00000000",
                "netAssetOfBtc": "0.00000000",
                "repayEnabled": True,
                "totalAsset": "0.00000000",
            },
            "quoteAsset": {
                "asset": "USDT",
                "borrowEnabled": True,
                "borrowed": "10.00000000",
                "free": "100.00000000",
                "interest": "0.00000000",
                "locked": "0.00000000",
                "netAsset": "90.00000000",
                "netAssetOfBtc": "0.00000000",
                "repayEnabled": True,
                "totalAsset": "0.00000000",
            },
            "symbol": "BTCUSDT",
            "isolatedCreated": True,
            "marginLevel": "10.00000000",
            "marginLevelStatus": "EXCESSIVE",
            "marginRatio": "10.00000000",
            "indexPrice": "10000.00000000",
            "liquidatePrice": "1000.00000000",
            "liquidateRate": "1.00000000",
            "tradeEnabled": True,
        }
    ],
    "totalAssetOfBtc": "0.00000000",
    "totalLiabilityOfBtc": "0.00000000",
    "totalNetAssetOfBtc": "0.00000000",
}

trading_fees = {
    "tradeFee": [
        {"symbol": "BTCUSDT", "maker": 0.9000, "taker": 1.0000},
    ],
    "success": True,
}


margin_order_creation = {
    "symbol": "BTCUSDT",
    "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
    "transactTime": 1507725176595,
    "price": "3998.3",
    "avgPrice": "3998.3",
    "origQty": "10.00000000",
    "executedQty": "10.00000000",
    "cummulativeQuoteQty": "10.00000000",
    "status": "FILLED",
    "timeInForce": "GTC",
    "type": "MARKET",
    "side": "SELL",
    "marginBuyBorrowAmount": 5,  # will not return if no margin trade happens
    "marginBuyBorrowAsset": "BTC",  # will not return if no margin trade happens
    "isIsolated": True,  # if isolated margin
    "fills": [
        {
            "price": "4000.00000000",
            "qty": "1.00000000",
            "commission": "4.00000000",
            "commissionAsset": "USDT",
        },
        {
            "price": "3999.00000000",
            "qty": "5.00000000",
            "commission": "19.99500000",
            "commissionAsset": "USDT",
        },
        {
            "price": "3998.00000000",
            "qty": "2.00000000",
            "commission": "7.99600000",
            "commissionAsset": "USDT",
        },
        {
            "price": "3997.00000000",
            "qty": "1.00000000",
            "commission": "3.99700000",
            "commissionAsset": "USDT",
        },
        {
            "price": "3995.00000000",
            "qty": "1.00000000",
            "commission": "3.99500000",
            "commissionAsset": "USDT",
        },
    ],
}

futures_order_creation = {
    "orderId": 3214109855,
    "symbol": "BTCUSDT",
    "status": "FILLED",
    "clientOrderId": "6MyYUkDJ4wU16daDkGXzy5",
    "price": "20000",
    "avgPrice": "20000",
    "origQty": "0.050",
    "executedQty": "0.050",
    "cumQty": "0.050",
    "cumQuote": "1000.0",
    "timeInForce": "GTC",
    "type": "MARKET",
    "reduceOnly": True,
    "closePosition": False,
    "side": "SELL",
    "positionSide": "BOTH",
    "stopPrice": "0",
    "workingType": "CONTRACT_PRICE",
    "priceProtect": False,
    "origType": "MARKET",
    "updateTime": 1663601948038
}

exchange_info = {
    "symbols": [
        {
            'symbol': 'BTCUSDT',
            'pair': 'BTCUSDT',
            'contractType': 'PERPETUAL',
            'deliveryDate': 4133404800000,
            'onboardDate': 1569398400000,
            'status': 'TRADING',
            'maintMarginPercent': '2.5000',
            'requiredMarginPercent': '5.0000',
            'baseAsset': 'BTC',
            'quoteAsset': 'USDT',
            'marginAsset': 'USDT',
            'pricePrecision': 2,
            'quantityPrecision': 3,
            'baseAssetPrecision': 8,
            'quotePrecision': 8,
            'underlyingType': 'COIN',
            'underlyingSubType': ['PoW'],
            'settlePlan': 0,
            'triggerProtect': '0.0500',
            'liquidationFee': '0.017500',
            'marketTakeBound': '0.05',
            'filters': [{'minPrice': '556.80',
                         'maxPrice': '4529764',
                         'filterType': 'PRICE_FILTER',
                         'tickSize': '0.10'},
                        {'stepSize': '0.001',
                         'filterType': 'LOT_SIZE',
                         'maxQty': '1000',
                         'minQty': '0.001'},
                        {'stepSize': '0.001',
                         'filterType': 'MARKET_LOT_SIZE',
                         'maxQty': '120',
                         'minQty': '0.001'},
                        {'limit': 200, 'filterType': 'MAX_NUM_ORDERS'},
                        {'limit': 10, 'filterType': 'MAX_NUM_ALGO_ORDERS'},
                        {'notional': '5', 'filterType': 'MIN_NOTIONAL'},
                        {'multiplierDown': '0.9500',
                         'multiplierUp': '1.0500',
                         'multiplierDecimal': '4',
                         'filterType': 'PERCENT_PRICE'}],
            'orderTypes': ['LIMIT',
                           'MARKET',
                           'STOP',
                           'STOP_MARKET',
                           'TAKE_PROFIT',
                           'TAKE_PROFIT_MARKET',
                           'TRAILING_STOP_MARKET'],
            'timeInForce': ['GTC', 'IOC', 'FOK', 'GTX']
        }
    ]
}


account_balances = [
    {
        "accountAlias": "FzFzfWuXmYSguX",
        "asset": "BNB",
        "balance": "0.00002403",
        "crossWalletBalance": "0.00002403",
        "crossUnPnl": "0.00000000",
        "availableBalance": "0.00002403",
        "maxWithdrawAmount": "0.00002403",
        "marginAvailable": True,
        "updateTime": 1683267921083,
    },
    {
        "accountAlias": "FzFzfWuXmYSguX",
        "asset": "USDT",
        "balance": "10000",
        "crossWalletBalance": "1952.45550004",
        "crossUnPnl": "0.00000000",
        "availableBalance": "10000",
        "maxWithdrawAmount": "1952.45550004",
        "marginAvailable": True,
        "updateTime": 1704326426077,
    },
    {
        "accountAlias": "FzFzfWuXmYSguX",
        "asset": "USDC",
        "balance": "0.00000000",
        "crossWalletBalance": "0.00000000",
        "crossUnPnl": "0.00000000",
        "availableBalance": "0.00000000",
        "maxWithdrawAmount": "0.00000000",
        "marginAvailable": True,
        "updateTime": 0,
    },
    {
        "accountAlias": "FzFzfWuXmYSguX",
        "asset": "BUSD",
        "balance": "0.00000000",
        "crossWalletBalance": "0.00000000",
        "crossUnPnl": "0.00000000",
        "availableBalance": "0.00000000",
        "maxWithdrawAmount": "0.00000000",
        "marginAvailable": True,
        "updateTime": 0,
    },
    {
        "accountAlias": "FzFzfWuXmYSguX",
        "asset": "ETH",
        "balance": "0.00000000",
        "crossWalletBalance": "0.00000000",
        "crossUnPnl": "0.00000000",
        "availableBalance": "0.00000000",
        "maxWithdrawAmount": "0.00000000",
        "marginAvailable": True,
        "updateTime": 0,
    },
    {
        "accountAlias": "FzFzfWuXmYSguX",
        "asset": "BTC",
        "balance": "0.00000000",
        "crossWalletBalance": "0.00000000",
        "crossUnPnl": "0.00000000",
        "availableBalance": "0.00000000",
        "maxWithdrawAmount": "0.00000000",
        "marginAvailable": True,
        "updateTime": 0,
    },
]

positions_info = [
    {
        "symbol": "ETHUSDT",
        "positionAmt": "0.000",
        "entryPrice": "0.00000000",
        "breakEvenPrice": "0.00000000",
        "markPrice": "2273.38000000",
        "unRealizedProfit": "0.00000000",
        "liquidationPrice": "0.00000000",
        "leverage": "10",
        "maxNotionalValue": "30000000.00000000",
        "marginType": "isolated",
        "isolatedMargin": "0.00000000",
        "isAutoAddMargin": "false",
        "positionSide": "BOTH",
        "notional": "0.00000000",
        "isolatedWallet": "0.00000000",
        "updateTime": 1700955221617,
        "isolated": True,
        "adlQuantile": 0,
    },
    {
        "symbol": "BTCUSDT",
        "positionAmt": "0.017",
        "entryPrice": "0.00000000",
        "breakEvenPrice": "0.00000000",
        "markPrice": "43907.54607229",
        "unRealizedProfit": "0.00000000",
        "liquidationPrice": "0.00000000",
        "leverage": "1",
        "maxNotionalValue": "500000000.00000000",
        "marginType": "isolated",
        "isolatedMargin": "0.00000000",
        "isAutoAddMargin": "false",
        "positionSide": "BOTH",
        "notional": "0.00000000",
        "isolatedWallet": "0.00000000",
        "updateTime": 1704326426077,
        "isolated": True,
        "adlQuantile": 0,
    },
]


account_balance = {
    "feeTier": 0,
    "canTrade": True,
    "canDeposit": True,
    "canWithdraw": True,
    "tradeGroupId": -1,
    "updateTime": 0,
    "multiAssetsMargin": False,
    "totalInitialMargin": "159.79407305",
    "totalMaintMargin": "6.39176292",
    "totalWalletBalance": "592.02529444",
    "totalUnrealizedProfit": "-14.21773054",
    "totalMarginBalance": "577.80756390",
    "totalPositionInitialMargin": "159.79407305",
    "totalOpenOrderInitialMargin": "0.00000000",
    "totalCrossWalletBalance": "420.23896009",
    "totalCrossUnPnl": "0.00000000",
    "availableBalance": "420.23896009",
    "maxWithdrawAmount": "420.23896009",
    "assets": [
        {
            "asset": "ETH",
            "walletBalance": "0.00000000",
            "unrealizedProfit": "0.00000000",
            "marginBalance": "0.00000000",
            "maintMargin": "0.00000000",
            "initialMargin": "0.00000000",
            "positionInitialMargin": "0.00000000",
            "openOrderInitialMargin": "0.00000000",
            "maxWithdrawAmount": "0.00000000",
            "crossWalletBalance": "0.00000000",
            "crossUnPnl": "0.00000000",
            "availableBalance": "0.00000000",
            "marginAvailable": True,
            "updateTime": 0,
        },
        {
            "asset": "BTC",
            "walletBalance": "0.02533569",
            "unrealizedProfit": "0.00000000",
            "marginBalance": "0.02533569",
            "maintMargin": "0.00000000",
            "initialMargin": "0.00000000",
            "positionInitialMargin": "0.00000000",
            "openOrderInitialMargin": "0.00000000",
            "maxWithdrawAmount": "0.02533569",
            "crossWalletBalance": "0.02533569",
            "crossUnPnl": "0.00000000",
            "availableBalance": "0.02533569",
            "marginAvailable": True,
            "updateTime": 1706031109043,
        },
        {
            "asset": "BNB",
            "walletBalance": "2.70887934",
            "unrealizedProfit": "0.00000000",
            "marginBalance": "2.70887934",
            "maintMargin": "0.00000000",
            "initialMargin": "0.00000000",
            "positionInitialMargin": "0.00000000",
            "openOrderInitialMargin": "0.00000000",
            "maxWithdrawAmount": "2.70887934",
            "crossWalletBalance": "2.70887934",
            "crossUnPnl": "0.00000000",
            "availableBalance": "2.70887934",
            "marginAvailable": True,
            "updateTime": 1706923492742,
        },
        {
            "asset": "USDT",
            "walletBalance": "592.02529444",
            "unrealizedProfit": "-14.21773054",
            "marginBalance": "577.80756390",
            "maintMargin": "6.39176292",
            "initialMargin": "159.79407305",
            "positionInitialMargin": "159.79407305",
            "openOrderInitialMargin": "0.00000000",
            "maxWithdrawAmount": "420.23896009",
            "crossWalletBalance": "420.23896009",
            "crossUnPnl": "0.00000000",
            "availableBalance": "420.23896009",
            "marginAvailable": True,
            "updateTime": 1706901204164,
        },
        {
            "asset": "USDC",
            "walletBalance": "0.00000000",
            "unrealizedProfit": "0.00000000",
            "marginBalance": "0.00000000",
            "maintMargin": "0.00000000",
            "initialMargin": "0.00000000",
            "positionInitialMargin": "0.00000000",
            "openOrderInitialMargin": "0.00000000",
            "maxWithdrawAmount": "0.00000000",
            "crossWalletBalance": "0.00000000",
            "crossUnPnl": "0.00000000",
            "availableBalance": "0.00000000",
            "marginAvailable": True,
            "updateTime": 0,
        },
        {
            "asset": "BUSD",
            "walletBalance": "0.00000000",
            "unrealizedProfit": "0.00000000",
            "marginBalance": "0.00000000",
            "maintMargin": "0.00000000",
            "initialMargin": "0.00000000",
            "positionInitialMargin": "0.00000000",
            "openOrderInitialMargin": "0.00000000",
            "maxWithdrawAmount": "0.00000000",
            "crossWalletBalance": "0.00000000",
            "crossUnPnl": "0.00000000",
            "availableBalance": "0.00000000",
            "marginAvailable": True,
            "updateTime": 0,
        },
    ],
    "positions": [{
        "symbol": "BTCUSDT",
        "initialMargin": "160",
        "maintMargin": "6.4",
        "unrealizedProfit": "-15",
        "positionInitialMargin": "160",
        "openOrderInitialMargin": "0.00000000",
        "leverage": "10",
        "isolated": True,
        "entryPrice": "42803.32432433",
        "breakEvenPrice": "42803.32432433",
        "maxNotional": "40000000.00000000",
        "positionSide": "BOTH",
        "positionAmt": "-0.035",
        "notional": "-1600",
        "isolatedWallet": "170",
        "updateTime": 1706923492742,
        "bidNotional": "0.00000000",
        "askNotional": "0.00000000",
    }, {
        "symbol": "ETHUSDT",
        "initialMargin": "15",
        "maintMargin": "6",
        "unrealizedProfit": "30",
        "positionInitialMargin": "15",
        "openOrderInitialMargin": "0.00000000",
        "leverage": "10",
        "isolated": True,
        "entryPrice": "4283.32432433",
        "breakEvenPrice": "4280.32432433",
        "maxNotional": "40000000.00000000",
        "positionSide": "BOTH",
        "positionAmt": "-0.4",
        "notional": "-1500",
        "isolatedWallet": "171.78633435",
        "updateTime": 1706923492742,
        "bidNotional": "0.00000000",
        "askNotional": "0.00000000",
    }],
}

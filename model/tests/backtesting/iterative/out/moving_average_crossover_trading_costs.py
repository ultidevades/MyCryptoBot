from pandas import Timestamp

expected_performance = 1.003375
expected_outperformance = -0.003015

expected_results = [
    {
        "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
        "open": 55550.89,
        "high": 56087.68,
        "low": 55550.89,
        "close": 55932.48,
        "volume": 692.924319,
        "quote_volume": 38726480.58078431,
        "trades": 16507,
        "taker_buy_asset_volume": 411.223017,
        "taker_buy_quote_volume": 22979821.33981915,
        "returns": 0,
        "SMA_S": 55565.7,
        "SMA_L": 55489.95428571429,
        "position": 1,
        "strategy_returns": 0.0,
        "strategy_returns_tc": -0.003,
        "accumulated_returns": 1.0068418286158654,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 0.997004495503373,
    },
    {
        "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
        "open": 55932.48,
        "high": 56333.0,
        "low": 55932.48,
        "close": 56264.93,
        "volume": 603.660118,
        "quote_volume": 33896505.6971466,
        "trades": 14656,
        "taker_buy_asset_volume": 356.915883,
        "taker_buy_quote_volume": 20037884.70780964,
        "returns": 0.005926179097336494,
        "SMA_S": 55784.692500000005,
        "SMA_L": 55615.09285714285,
        "position": 1,
        "strategy_returns": 0.005926179097336494,
        "strategy_returns_tc": 0.005926179097336494,
        "accumulated_returns": 1.0128262685320526,
        "accumulated_strategy_returns": 1.0059437736356407,
        "accumulated_strategy_returns_tc": 1.0029304645383612,
    },
    {
        "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
        "open": 56260.11,
        "high": 56317.43,
        "low": 56118.31,
        "close": 56168.82,
        "volume": 370.500359,
        "quote_volume": 20822485.25288953,
        "trades": 8616,
        "taker_buy_asset_volume": 178.075904,
        "taker_buy_quote_volume": 10007121.78892216,
        "returns": -0.00170962942015996,
        "SMA_S": 55979.6575,
        "SMA_L": 55726.50142857143,
        "position": 1,
        "strategy_returns": -0.00170962942015996,
        "strategy_returns_tc": -0.00170962942015996,
        "accumulated_returns": 1.0110961902636069,
        "accumulated_strategy_returns": 1.0042254518304927,
        "accumulated_strategy_returns_tc": 1.0012172899739071,
    },
    {
        "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
        "open": 56168.82,
        "high": 56269.99,
        "low": 56080.96,
        "close": 56191.11,
        "volume": 324.51432,
        "quote_volume": 18225087.41727558,
        "trades": 8352,
        "taker_buy_asset_volume": 145.064381,
        "taker_buy_quote_volume": 8146012.47892439,
        "returns": 0.0003967606653441501,
        "SMA_S": 56139.335,
        "SMA_L": 55841.09428571428,
        "position": 1,
        "strategy_returns": 0.0003967606653441501,
        "strategy_returns_tc": 0.0003967606653441501,
        "accumulated_returns": 1.0114974330541975,
        "accumulated_strategy_returns": 1.0046239680414673,
        "accumulated_strategy_returns_tc": 1.0016146124277796,
    },
    {
        "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
        "open": 56191.11,
        "high": 56200.0,
        "low": 56107.98,
        "close": 56145.0,
        "volume": 254.091606,
        "quote_volume": 14265787.89818125,
        "trades": 6455,
        "taker_buy_asset_volume": 134.1124,
        "taker_buy_quote_volume": 7529521.30623853,
        "returns": -0.0008209293091875578,
        "SMA_S": 56192.465000000004,
        "SMA_L": 55949.09999999999,
        "position": 1,
        "strategy_returns": -0.0008209293091875578,
        "strategy_returns_tc": -0.0008209293091875578,
        "accumulated_returns": 1.0106674059086556,
        "accumulated_strategy_returns": 1.0037995812093439,
        "accumulated_strategy_returns_tc": 1.000792695050119,
    },
    {
        "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
        "open": 56145.0,
        "high": 56211.7,
        "low": 56106.97,
        "close": 56182.11,
        "volume": 270.145731,
        "quote_volume": 15171017.18758856,
        "trades": 7707,
        "taker_buy_asset_volume": 168.231118,
        "taker_buy_quote_volume": 9447425.0774598,
        "returns": 0.0006607487960858385,
        "SMA_S": 56171.759999999995,
        "SMA_L": 56062.40714285715,
        "position": 1,
        "strategy_returns": 0.0006607487960858385,
        "strategy_returns_tc": 0.0006607487960858385,
        "accumulated_returns": 1.0113354238520749,
        "accumulated_strategy_returns": 1.0044630597463227,
        "accumulated_strategy_returns_tc": 1.0014541861341568,
    },
    {
        "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
        "open": 56182.12,
        "high": 56299.78,
        "low": 56172.09,
        "close": 56289.89,
        "volume": 298.797415,
        "quote_volume": 16804824.55255641,
        "trades": 9000,
        "taker_buy_asset_volume": 139.83665,
        "taker_buy_quote_volume": 7864202.02549528,
        "returns": 0.0019165664875115606,
        "SMA_S": 56202.027500000004,
        "SMA_L": 56167.76285714285,
        "position": 0,
        "strategy_returns": 0.0019165664875115606,
        "strategy_returns_tc": -0.0010834335124884395,
        "accumulated_returns": 1.0132755740526063,
        "accumulated_strategy_returns": 1.0063900259741747,
        "accumulated_strategy_returns_tc": 1.000369764663036,
    },
]

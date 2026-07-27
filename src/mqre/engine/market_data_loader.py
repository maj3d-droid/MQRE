from datetime import datetime, timezone

import requests

from mqre.engine.market_data import Candle, validate_candles


BINANCE_BASE_URL = "https://data-api.binance.vision"
KLINES_ENDPOINT = "/api/v3/klines"

SUPPORTED_TIMEFRAMES = {
    "4H": "4h",
    "1D": "1d",
}


def fetch_candles(
    symbol: str,
    timeframe: str,
    limit: int = 200,
) -> list[Candle]:
    if timeframe not in SUPPORTED_TIMEFRAMES:
        raise ValueError(
            f"Unsupported timeframe: {timeframe}. "
            f"Supported values: {list(SUPPORTED_TIMEFRAMES)}"
        )

    if limit < 1 or limit > 1000:
        raise ValueError("Limit must be between 1 and 1000.")

    params = {
        "symbol": symbol.upper(),
        "interval": SUPPORTED_TIMEFRAMES[timeframe],
        "limit": limit,
    }

    response = requests.get(
        f"{BINANCE_BASE_URL}{KLINES_ENDPOINT}",
        params=params,
        timeout=15,
    )
    response.raise_for_status()

    raw_candles = response.json()

    candles = [
        Candle(
            timestamp=datetime.fromtimestamp(
                candle[0] / 1000,
                tz=timezone.utc,
            ),
            open=float(candle[1]),
            high=float(candle[2]),
            low=float(candle[3]),
            close=float(candle[4]),
            volume=float(candle[5]),
        )
        for candle in raw_candles
    ]

    validate_candles(candles)

    return candles


def print_loader_status() -> None:
    print("MQRE Market Data Loader")
    print("-----------------------")

    for timeframe in ("1D", "4H"):
        candles = fetch_candles(
            symbol="BTCUSDT",
            timeframe=timeframe,
            limit=5,
        )

        latest = candles[-1]

        print(f"{timeframe}: {len(candles)} candles loaded")
        print(f"Latest candle: {latest.timestamp.isoformat()}")
        print(f"Latest close: {latest.close:,.2f}")
        print()


if __name__ == "__main__":
    print_loader_status()
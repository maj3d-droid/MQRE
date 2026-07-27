from dataclasses import dataclass
from datetime import datetime
from typing import Iterable


@dataclass(frozen=True)
class Candle:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def validate(self) -> None:
        if self.high < self.low:
            raise ValueError("Candle high cannot be below candle low.")

        if self.high < max(self.open, self.close):
            raise ValueError("Candle high cannot be below open or close.")

        if self.low > min(self.open, self.close):
            raise ValueError("Candle low cannot be above open or close.")

        if self.volume < 0:
            raise ValueError("Candle volume cannot be negative.")


def validate_candles(candles: Iterable[Candle]) -> None:
    previous_timestamp: datetime | None = None

    for candle in candles:
        candle.validate()

        if (
            previous_timestamp is not None
            and candle.timestamp <= previous_timestamp
        ):
            raise ValueError(
                "Candles must be ordered from oldest to newest."
            )

        previous_timestamp = candle.timestamp


def print_market_data_status() -> None:
    print("MQRE Market Data Engine")
    print("-----------------------")
    print("Status: operational")
    print("Supported timeframes:")
    print("- Daily")
    print("- 4H")


if __name__ == "__main__":
    print_market_data_status()
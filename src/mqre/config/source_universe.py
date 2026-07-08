"""
MQRE Source Universe

This file defines the core research sources used by the MQRE Bitcoin Morning Brief.
Sources are grouped by research category so the engine can later score evidence
from macro, liquidity, commodities, on-chain, derivatives, institutional flows,
sentiment, and analyst viewpoints.
"""

SOURCE_UNIVERSE = {
    "macro_liquidity": [
        "DXY",
        "US 10Y yield",
        "US 2Y yield",
        "Federal Reserve liquidity",
        "Treasury General Account",
        "Reverse Repo Facility",
        "S&P 500",
        "Nasdaq 100",
        "VIX",
        "US economic calendar",
    ],

    "commodities_cross_asset": [
        "Gold",
        "Silver",
        "Oil",
        "Copper",
    ],

    "crypto_market_structure": [
        "Bitcoin spot price",
        "Bitcoin daily chart",
        "Bitcoin weekly chart",
        "BTC support and resistance",
        "BTC trend structure",
        "BTC volatility",
    ],

    "derivatives": [
        "BTC funding rates",
        "BTC open interest",
        "BTC liquidations",
        "BTC options skew",
        "CME Bitcoin futures positioning",
    ],

    "on_chain": [
        "Glassnode",
        "CryptoQuant",
        "Arkham",
        "Exchange inflows",
        "Exchange outflows",
        "Whale activity",
        "Long-term holder behaviour",
        "Short-term holder behaviour",
    ],

    "institutional": [
        "Bitcoin ETF flows",
        "BlackRock Bitcoin ETF",
        "Fidelity Bitcoin ETF",
        "Grayscale Bitcoin ETF",
        "MicroStrategy Bitcoin holdings",
    ],

    "sentiment": [
        "Bitcoin Fear and Greed Index",
        "Crypto news sentiment",
        "Retail search interest",
        "Social sentiment",
    ],

    "analysts_contrarian": [
        "Lyn Alden",
        "Henrik Zeberg",
        "Luke Gromen",
        "Jeff Snider",
        "Michael Burry",
        "Peter Schiff",
        "Gerald Celente",
        "David Morgan",
        "Daniela Cambone",
        "David Lin",
        "Kitco News",
        "Trends Journal",
        "Soar Financially",
    ],

    "analysts_crypto": [
        "Benjamin Cowen",
        "Sasha Yanshin",
        "Coin Bureau",
        "Altcoin Buzz",
        "Gareth Soloway",
        "Patrick Karim",
    ],
}

"""
MQRE Source Loader

Loads the configured MQRE source universe and provides simple helper functions
for checking which research categories and sources are available.
"""

from mqre.config.source_universe import SOURCE_UNIVERSE


def get_source_categories():
    """Return all source categories."""
    return list(SOURCE_UNIVERSE.keys())


def get_sources_for_category(category_name):
    """Return sources for a specific category."""
    return SOURCE_UNIVERSE.get(category_name, [])


def count_sources():
    """Return total number of configured sources."""
    return sum(len(sources) for sources in SOURCE_UNIVERSE.values())


def print_source_summary():
    """Print a readable source universe summary."""
    print("MQRE Source Universe Loaded")
    print("---------------------------")

    for category, sources in SOURCE_UNIVERSE.items():
        print(f"{category}: {len(sources)} sources")

    print("---------------------------")
    print(f"Total sources: {count_sources()}")


if __name__ == "__main__":
    print_source_summary()

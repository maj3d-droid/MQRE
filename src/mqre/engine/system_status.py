from mqre.config.source_universe import SOURCE_UNIVERSE


def build_system_status() -> dict:
    category_counts = {
        category: len(sources)
        for category, sources in SOURCE_UNIVERSE.items()
    }

    total_sources = sum(category_counts.values())

    return {
        "system": "MQRE",
        "status": "operational",
        "source_categories": category_counts,
        "total_sources": total_sources,
    }


def print_system_status() -> None:
    status = build_system_status()

    print("MQRE System Status")
    print("------------------")
    print(f"Status: {status['status']}")
    print(f"Total sources: {status['total_sources']}")
    print()

    for category, count in status["source_categories"].items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    print_system_status()
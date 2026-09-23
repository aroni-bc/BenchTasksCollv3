from src.price_tracker import PriceTracker


def evaluate():
    tracker = PriceTracker()
    result = tracker.run()
    return result


if __name__ == "__main__":
    print(evaluate())

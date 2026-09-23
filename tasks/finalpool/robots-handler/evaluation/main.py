from src.robots_handler import RobotsHandler


def evaluate():
    handler = RobotsHandler()
    result = handler.run()
    return result


if __name__ == "__main__":
    print(evaluate())

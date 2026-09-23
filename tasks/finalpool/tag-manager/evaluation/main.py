from src.tag_manager import TagManager


def evaluate():
    manager = TagManager()
    result = manager.run()
    return result


if __name__ == "__main__":
    print(evaluate())

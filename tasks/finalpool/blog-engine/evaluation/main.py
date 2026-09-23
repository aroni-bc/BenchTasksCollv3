from src.blog_engine import BlogEngine


def evaluate():
    engine = BlogEngine()
    result = engine.run()
    return result


if __name__ == "__main__":
    print(evaluate())

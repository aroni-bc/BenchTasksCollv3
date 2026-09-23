from src.cms_builder import CMSBuilder


def evaluate():
    builder = CMSBuilder()
    result = builder.run()
    return result


if __name__ == "__main__":
    print(evaluate())

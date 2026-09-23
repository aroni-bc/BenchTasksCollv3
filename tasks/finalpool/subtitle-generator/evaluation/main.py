from src.subtitle_generator import SubtitleGenerator


def evaluate():
    generator = SubtitleGenerator()
    result = generator.run()
    return result


if __name__ == "__main__":
    print(evaluate())

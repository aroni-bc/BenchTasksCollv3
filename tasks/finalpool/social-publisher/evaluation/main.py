from src.social_publisher import SocialPublisher


def evaluate():
    publisher = SocialPublisher()
    result = publisher.run()
    return result


if __name__ == "__main__":
    print(evaluate())

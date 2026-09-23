from src.content_scheduler import ContentScheduler


def evaluate():
    scheduler = ContentScheduler()
    result = scheduler.run()
    return result


if __name__ == "__main__":
    print(evaluate())

from src.media_organizer import MediaOrganizer


def evaluate():
    organizer = MediaOrganizer()
    result = organizer.run()
    return result


if __name__ == "__main__":
    print(evaluate())

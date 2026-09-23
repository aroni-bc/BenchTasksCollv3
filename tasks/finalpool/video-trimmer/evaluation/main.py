from src.video_trimmer import VideoTrimmer


def evaluate():
    trimmer = VideoTrimmer()
    result = trimmer.run()
    return result


if __name__ == "__main__":
    print(evaluate())

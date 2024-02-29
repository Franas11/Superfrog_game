import time


class Timer:
    def __init__(self) -> None:
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        if self.start_time is None:
            return None
        elapsed_time = time.time() - self.start_time
        return elapsed_time

    def get_minutes(self):
        elapsed_time = self.get_elapsed_time()
        if elapsed_time is None:
            return None
        minutes = int(elapsed_time // 60)
        return minutes

    def get_seconds(self):
        elapsed_time = self.get_elapsed_time()
        if elapsed_time is None:
            return None
        seconds = int(elapsed_time % 60)
        return seconds

from enum import Enum, auto

class Progress(Enum):
    DONE = auto(),
    IN_PROGRESS = auto(),
    NOT_DONE = auto()

class Task:
    def __init__(self, acronym, description, date, time, progress = Progress.NOT_DONE):
        self.acronym = acronym.upper().ljust(3, '#')[:3]
        self.description = description
        self.date = date
        self.time = time
        self.progress = progress

    def print_task(self):
        print(f"{self.acronym} - {self.description}")
        print(f"{self.date}; {self.time}")
        print(f"{self.progress.name}")
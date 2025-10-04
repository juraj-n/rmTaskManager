from enum import Enum, auto

class Status(Enum):
    DONE = "done",
    IN_PROGRESS = "in_progress",
    TO_DO = "todo"

class Task:
    def __init__(self, id, description, created_at, updated_at, status = Status.TO_DO):
        self.id = id,
        self.description = description,
        self.created_at = created_at,
        self.updated_at = updated_at,
        self.status = status

    def print_task(self):
        print(f"{self.description} - {self.status}")
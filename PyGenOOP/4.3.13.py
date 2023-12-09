from typing import NoReturn


class Todo:
    def __init__(self):
        self.things: list[tuple[str, int]] = []

    def add(self, task, priority) -> NoReturn:
        self.things.append((task, priority))

    def get_by_priority(self, priority: int):
        if self.things:
            return [task[0] for task in self.things if task[1] == priority]
        return []

    def get_low_priority(self):
        if self.things:
            min_priority: int = min(self.things, default=[], key=lambda task: task[1])[1]
            return [task[0] for task in self.things if task[1] == min_priority]
        return []

    def get_high_priority(self):
        if self.things:
            max_priority: int = max(self.things, default=[], key=lambda task: task[1])[1]
            return [task[0] for task in self.things if task[1] == max_priority]
        return []

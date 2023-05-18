
class Task:
    def __init__(self, title, importance=1, duration=1, desc=""):
        self.title = title
        self.importance = importance
        self.duration = duration
        self.desc = desc

    def __str__(self):
        return f'{self.title}: {self.desc}'

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise NotImplementedError(
                "Equality only implemented on type Task.")
        return self.title == other.title

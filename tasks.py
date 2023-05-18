
class Task:
    def __init__(self, title, importance, duration, desc):
        self.title = title
        self.importance = importance
        self.duration = duration
        self.desc = desc

    def __str__(self):
        return f'{self.title}: {self.desc}'

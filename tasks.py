from datetime import datetime
import json


class TaskEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, Task):
            return vars(arg)
        elif isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)


class Task:
    def __init__(self, title, importance=1, duration=1, desc=""):
        self.title = title
        self.importance = importance
        self.duration = duration
        self.desc = desc
        self.registered = datetime.utcnow()

    def __str__(self):
        return f'{self.title}: {self.desc}'

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise NotImplementedError(
                "Equality only implemented on type Task.")
        return self.title == other.title


def main():
    task = Task('test')
    print(json.dumps(task, cls=TaskEncoder, indent=2))


if __name__ == "__main__":
    main()

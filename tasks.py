from datetime import date
import json


class Task:
    def __init__(self, title, importance=1, duration=1, desc=None, registered=None):
        self.title = title
        self.importance = importance
        self.duration = duration
        self.desc = desc
        self.registered = registered
        if self.desc is None:
            self.desc = '(No description)'
        if self.registered is None:
            self.registered = date.today()
        if isinstance(self.registered, str):
            try:
                self.registered = date.fromisoformat(self.registered)
            except Exception as ex:
                raise ex('Invalid date string')

    def __str__(self):
        if self.desc:
            return f'{self.title}: {self.desc}'
        else:
            return f'{self.title}'

    def __repr__(self):
        return 'Task(title={0}, importance={1}, duration={2}, desc={3}, registered={4}'.format(self.title, self.importance, self.duration, self.desc, self.registered)

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise NotImplementedError(
                "Equality only implemented on type Task.")
        return self.title == other.title


class TaskEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, Task):
            return vars(arg)
        elif isinstance(arg, date):
            return date.isoformat(arg)
        else:
            return super().default(arg)


class TaskDecoder(json.JSONDecoder):
    def decode(self, arg):
        # obj = json.loads(arg)
        if isinstance(arg, str):
            obj = json.loads(arg)
        else:
            obj = arg

        return Task(**obj)


def main():
    task = Task('test', desc='testing')
    j_task = json.dumps(task, cls=TaskEncoder, indent=2)
    print(j_task)
    d_task = json.loads(j_task, cls=TaskDecoder)
    print(d_task)
    j_task = json.dumps(task, cls=TaskEncoder, indent=2)
    print(j_task)
    d_task = json.loads(j_task, cls=TaskDecoder)
    print(d_task)
    j_task = json.dumps(task, cls=TaskEncoder, indent=2)
    print(j_task)
    d_task = json.loads(j_task, cls=TaskDecoder)
    print(d_task)


if __name__ == "__main__":
    main()

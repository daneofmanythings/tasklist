from datetime import date
import json


class Task:
    def __init__(
            self,
            title=None,
            importance=None,
            duration=None,
            desc=None,
            registered=None):
        self.title = title
        self.importance = importance
        self.duration = duration
        self.desc = desc
        self._registered = registered
        if self.desc is None:
            self.desc = '(No description)'
        if self._registered is None:
            self._registered = date.today()
        if isinstance(self._registered, str):
            try:
                self._registered = date.fromisoformat(self._registered)
            except Exception as ex:
                raise ex('Invalid date string')

    def __str__(self):
        result = ""
        for attr, val in vars(self).items():
            if attr.startswith('_'):
                continue
            result += f'{attr}: {val}\n'
        return result

    def __repr__(self):
        return 'Task(title={0}, importance={1}, duration={2}, desc={3}, registered={4}'.format(self.title, self.importance, self.duration, self.desc, self._registered)

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

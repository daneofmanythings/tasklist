from functools import total_ordering
from datetime import date
import json


@total_ordering
class Task:
    def __init__(self, title=None, length='0', notes=None, registered=None):

        self.title = title
        self.length = length
        self.notes = notes
        self.registered = registered

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        try:
            if int(val) >= 0:
                self._length = val
            else:
                raise ValueError('Length must be a positive integer')
        except Exception:
            raise ValueError('Length must be a positive integer')

    @property
    def registered(self):
        return self._registered

    @registered.setter
    def registered(self, val):
        if not val:
            self._registered = date.today()
        else:
            try:
                self._registered = date.fromisoformat(val)
            except Exception:
                raise ValueError(f'Invalid date string: {val}')

    def listify(self):
        result = list()
        for attr, val in vars(self).items():
            result.append(f"{attr.replace('_', '')}: {val}")
        return result

    def __str__(self):
        result = ""
        for attr, val in vars(self).items():
            result += f'{attr}: {val}\n'
        return result

    def __repr__(self):
        return 'Task(title={0}, importance={1}, duration={2}, desc={3}, registered={4}'.format(self.title, self.importance, self.length, self.notes, self.registered)

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise NotImplementedError(
                "Equality only implemented on type Task.")
        return self.title == other.title

    def __lt__(self, other):
        if not isinstance(other, Task):
            raise NotImplementedError(
                "Comparison only implemented on type Task.")
        return self.title <= other.title


class TaskEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, Task):
            return {k.replace('_', ''): v for k, v in vars(arg).items()}
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


def ser_deser_test():
    task = Task('test', notes='testing')
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


def property_testing():
    t = Task()
    for val in vars(t):
        val = val.replace('_', '')
        while True:
            response = input(f'{val}? >> ')
            try:
                setattr(t, val, response)
                break
            except ValueError as e:
                print(e)
                continue


def date_testing():
    t = Task()
    while True:
        r = input('date >> ')
        try:
            setattr(t, 'registered', r)
            break
        except ValueError as e:
            print(e)
            continue

    print(vars(t))


if __name__ == "__main__":
    date_testing()

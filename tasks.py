from datetime import date
import json


class Task:
    def __init__(self, title=None, length='0', notes=None, date_=None):

        self.title = title
        self.length = length
        self.notes = notes
        self._date = date_

        if self._date is None:
            self._date = date.today()
        if isinstance(self._date, str):
            try:
                self._date = date.fromisoformat(self._date)
            except Exception as ex:
                raise ex('Invalid date string')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        if val.isdigit() and int(val) <= 0:
            self._length = val
        else:
            raise TypeError('length must be a positive integer')

    def __str__(self):
        result = ""
        for attr, val in vars(self).items():
            if attr.startswith('_'):
                continue
            result += f'{attr}: {val}\n'
        return result

    def __repr__(self):
        return 'Task(title={0}, importance={1}, duration={2}, desc={3}, registered={4}'.format(self.title, self.importance, self.length, self.notes, self._date)

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


if __name__ == "__main__":
    main()

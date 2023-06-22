from functools import total_ordering
from collections import defaultdict
from datetime import date, timedelta
import json


def putter(val):
    return lambda: val


@total_ordering
class Task:

    recurrence_responses = {
        'y': True,
        'yes': True,
        'n': False,
        'no': False
    }

    private_attrs = (
        '_created_date',
        '_last_completed'
    )

    def __init__(
            self,
            title=None,
            notes=None,
            length='0',
            start_date=None,
            period=None,
            strict_recurrence=None,
            created_date=None,
            last_completed=None,

    ):

        self.title: str = title
        self.notes: str = notes
        self.length: int = length  # validates to be non-negative
        self.start_date: date = start_date  # defaults to today()
        self.period: int = period  # validates to be non-negative
        self.strict_recurrence: bool = strict_recurrence  # validates to be bool
        self.created_date: date = created_date
        self.last_completed: date = last_completed

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        if val is None or val == '\n':
            self._length = 0
        else:
            try:
                int_val = int(val)
                if int_val >= 0:
                    self._length = int_val
                    return
            except Exception:
                raise ValueError('Length must be a non-negative integer (1)')

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, val):
        if not val:
            self._start_date = date.today()
        elif isinstance(val, date):
            self._created_date = val
        else:
            try:
                self._start_date = date.fromisoformat(val)
            except Exception:
                raise ValueError(f'Invalid date string (YYYY-MM-DD): "{val}"')

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, val):
        if val is None or val == '\n':
            self._period = 0
        else:
            try:
                int_val = int(val)
                if int_val >= 0:
                    self._period = int_val
                    return
            except Exception:
                raise ValueError('period must be a non-negative integer (1)')

    @property
    def strict_recurrence(self):
        return self._strict_recurrence

    @strict_recurrence.setter
    def strict_recurrence(self, val):
        if val is True or val is False:
            self._strict_recurrence = val
        elif val is None:
            self._strict_recurrence = False
        else:
            try:
                self._strict_recurrence = self.recurrence_responses[val.strip(
                )]
            except KeyError:
                raise ValueError(
                    'Acceptable values: ' + f'{list(self.recurrence_responses.keys())}')

    @ property
    def created_date(self):
        return self._created_date

    @ created_date.setter
    def created_date(self, val):
        if not val:
            self._created_date = date.today()
        elif isinstance(val, date):
            self._created_date = val
        else:
            try:
                self._created_date = date.fromisoformat(val)
            except Exception:
                raise ValueError(f'Invalid date string (YYYY-MM-DD): "{val}"')

    @ property
    def last_completed(self):
        return self._last_completed

    @ last_completed.setter
    def last_completed(self, val):
        if val is None:
            self._last_completed = None
        else:
            self._last_completed = date.today()

    def public_listify(self):
        result = list()
        for attr, val in vars(self).items():
            if attr in self.private_attrs:
                continue
            result.append(f"{attr.removeprefix('_')}: {val}")
        return result

    def listify(self):
        result = list()
        for attr, val in vars(self).items():
            result.append(f"{attr.removeprefix('_')}: {val}")
        return result

    def public_vars(self):
        return {attr: val for attr, val in vars(self).items() if attr not in self.private_attrs}

    def __str__(self):
        result = ""
        for attr, val in vars(self).items():
            result += f'{attr}: {val}\n'
        return result

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.title == other.title
        elif isinstance(other, str):
            return self.title == other
        else:
            raise NotImplementedError(
                "Equality only implemented on type Task.")

    def __lt__(self, other):
        if not isinstance(other, Task):
            raise NotImplementedError(
                "Comparison only implemented on type Task.")
        return self.title <= other.title

    def __copy__(self):
        return Task(**{k.removeprefix('_'): v for k, v in vars(self).items()})


class TaskEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, Task):
            return {k.removeprefix('_'): v for k, v in vars(arg).items()}
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


####################
# HELPER FUNCTIONS #
####################


def is_due(task):
    if task.period:
        if task.last_completed is None:
            return True

        if task.strict_recurrence:
            # how far off the last completion was from periods cadence
            offset = (
                task.last_completed - task.start_date).days % task.period
            # the latest cadenced day
            offset_date = task.last_completed - timedelta(days=offset)
            return (date.today() - offset_date).days >= task.period
        else:
            return (date.today() - task.last_completed).days >= task.period

    # if there is no period, strict doesn't matter
    return (date.today() - task.start_date).days >= 0


def testing():
    T = Task(
        title='a',
        notes='a',
        length=1,
        start_date='2023-06-01',
        period=15,
        strict_recurrence=True,
        created_date=None,
    )
    T._last_completed = date.fromisoformat('2023-06-11')
    print(list(filter(is_due, [T])))


if __name__ == "__main__":
    testing()

from functools import total_ordering
from datetime import date, datetime, timedelta
import json


@total_ordering
class Task:

    recurrence_responses = {
        't': True,
        'true': True,
        'f': False,
        'false': False
    }

    private_attrs = (
        '_created_date',
        '_last_completed',
    )

    def __init__(
            self,
            title=None,
            notes=None,
            length='0',
            start_date=None,
            deadline=None,
            period=None,
            strict_recurrence=None,
            created_date=None,
            last_completed=None,

    ):

        self.title: str = title
        self.notes: str = notes
        self.length: int = length  # validates to be non-negative
        self.start_date: date = start_date  # defaults to today()
        self.deadline: date = deadline  # defaults to None
        self.period: int = period  # validates to be non-negative
        self.strict_recurrence: bool = strict_recurrence  # validates to be bool
        self.created_date: date = created_date
        self.last_completed: date = last_completed

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        if not val:
            self._title = "task-" + str(abs(hash(datetime.utcnow())))
        else:
            self._title = val

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        if not val:
            self._length = 0
        else:
            try:
                int_val = int(val)
                if int_val >= 0:
                    self._length = int_val
                    return
            except Exception:
                raise ValueError('Length must be a non-negative integer')

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
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, val):
        if not val:
            self._deadline = None
        elif isinstance(val, date):
            self._deadline = val
        else:
            try:
                self._deadline = date.fromisoformat(val)
            except Exception:
                raise ValueError(f'Invalid date string (YYYY-MM-DD): "{val}"')

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, val):
        if not val:
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
        elif not val:
            self._strict_recurrence = False
        else:
            try:
                self._strict_recurrence = self.recurrence_responses[val.strip(
                )]
            except KeyError:
                raise ValueError(
                    'Acceptable values: ' + f'{list(self.recurrence_responses.keys())}')

    @property
    def created_date(self):
        return self._created_date

    @created_date.setter
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

    @property
    def last_completed(self):
        return self._last_completed

    @last_completed.setter
    def last_completed(self, val):
        try:
            self._last_completed = date.fromisoformat(val)
            return
        except (TypeError, ValueError):
            pass

        if val is None or isinstance(val, date):
            self._last_completed = val
        elif val == '':
            self._last_completed = date.today()
        else:
            raise ValueError(f'Invalid date string (YYYY-MM-DD): "{val}"')

    @property
    def is_due(self):
        if self.last_completed is None:
            if date.today() >= self.start_date:
                return True
            else:
                return False

        if self.period:

            if self.strict_recurrence:
                # how far off the last completion was from periods cadence
                offset = (
                    self.last_completed - self.start_date).days % self.period
                # the latest cadenced day
                offset_date = self.last_completed - timedelta(days=offset)
                return (date.today() - offset_date).days >= self.period
            else:
                return (date.today() - self.last_completed).days >= self.period

        return False

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


def testing():
    T = Task(
        title='a',
        notes='a',
        length=1,
        start_date='2023-05-23',
        period=15,
        strict_recurrence=True,
        created_date=None,
        last_completed='2023-06-21'
    )
    L = ([str(task) for task in [T] if task.is_due])
    for t in L:
        print(t)


if __name__ == "__main__":
    testing()

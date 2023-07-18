from datetime import datetime


class TasklistParameters:

    private_attrs = {
        'tags'
    }

    def __init__(self):
        self.title = datetime.utcnow()
        self.duration = 60
        self.tags = set()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        if not val:
            return
        try:
            self._title = str(val)
        except ValueError:
            raise ValueError("Title must have a string representation")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        if not val:
            return
        else:
            try:
                int_val = int(val)
                if int_val >= 0:
                    self._duration = int_val
                    return
            except Exception:
                raise ValueError('Duration must be a non-negative integer (1)')

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

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

from datetime import datetime


class TasklistParameters:

    def __init__(self):
        self.title = datetime.utcnow()
        self.duration = 60
        # self.tags = list()

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

    # @property
    # def tags(self):
    #     return self._tags
    #
    # @tags.setter
    # def tags(self, val):
    #     if isinstance(val, str):
    #         val_strip = val.strip()
    #         self._tags = list(set(val_strip.split(' ')))
    #     elif isinstance(val, list):
    #         self._tags = list(set(val))
    #     else:
    #         self._tags = list()

    def listify(self):
        result = list()
        for attr, val in vars(self).items():
            result.append(f"{attr.removeprefix('_')}: {val}")
        return result

    def public_vars(self):
        return {attr: val for attr, val in vars(self).items() if attr not in self.private_attrs}

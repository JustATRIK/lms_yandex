from datetime import datetime


class CheckedList:

    def __init__(self, *values):
        self._values = [] + list(values)

    def append(self, *data):
        if len(data) > 1:
            self._values.append(tuple(list(data) + [False]))
        else:
            self._values.append((data[0], False))

    def checked_values(self):
        return list(filter(lambda value: value[-1], self._values))

    def check(self, value):
        ind = -1
        for i, rest_value in enumerate(self._values):
            if rest_value[0] == value:
                ind = i

        if ind == -1:
            return

        mutable = list(self._values[ind])
        mutable[-1] = True

        self._values[ind] = tuple(mutable)

    def rest_values(self):
        return list(filter(lambda value: not value[-1], self._values))

    def values(self):
        return self._values


class ShoppingList(CheckedList):
    pass


class TODOList(CheckedList):

    def __init__(self, *values):
        super().__init__(*values)
        self._values.sort(key=lambda value: -value[1])

    def append(self, *data):
        super().append(*data)
        self._values.sort(key=lambda value: -value[1])


class Route(CheckedList):

    def append(self, *data):

        if len(self._values) == 0 or datetime.strptime(data[1], "%H:%M") > datetime.strptime(self._values[-1][1],
                                                                                             "%H:%M"):
            super().append(*data)

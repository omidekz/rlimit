import typing as t


class Core:
    def __init__(
        self,
        getter: t.Callable[[str, t.Any], t.Any]=None,
        setter: t.Callable[[str, t.Any], t.Any]=None
    ):
        if getter is None:
            getter = lambda key, default: self._inmemory.get(key, default)
        if setter is None:
            setter = lambda key, value: self._inmemory.update({key: value})
        self._inmemory = dict()
        self.getter = getter
        self.setter = setter

    def set(self, key, val):
        return self.setter(key, val)

    def get(self, key, default=None):
        return self.getter(key, default)

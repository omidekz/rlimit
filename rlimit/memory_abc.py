import abc


class BaseMemory(abc.ABC):
    @abc.abstractmethod
    def inc_call(self, key: str, ttl: float): ...

    @abc.abstractmethod
    def call_of(self, key: str) -> int: ...

    @abc.abstractmethod
    def exists(self, key: str) -> bool: ...

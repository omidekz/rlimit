import abc


class BaseMemory(abc.ABC):
    @abc.abstractmethod
    def inc_call(self, key: str, ttl: float):
        """
            increase the calls of key and dispatch after ttl (in seconds)
        """
        ...

    @abc.abstractmethod
    def call_of(self, key: str) -> int:
        """
            get the not dispatched calls of key
        """
        ...

    @abc.abstractmethod
    def exists(self, key: str) -> bool: ...

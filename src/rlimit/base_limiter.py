from typing import Callable, Union, ClassVar, Type
import functools
import uuid
from .memory_abc import BaseMemory
from .expiringdict_memory import ExpiringDictMemory

KeyType = Callable[[tuple, dict], str]
ExceptionType = Union[Type[BaseException], BaseException]


class BaseLimiter:
    times: int
    per: float
    key: KeyType = lambda *args, **kwargs: ''
    exception: ExceptionType
    memory: ClassVar[BaseMemory] = ExpiringDictMemory()

    def __init__(self, times: int, per: float, key: KeyType = lambda *args, **kwargs: '',
                 exception: ExceptionType = OverflowError):
        self.times = times
        self.per = per
        self.key = key
        self.exception = exception

    def __call__(self, func):
        base_key = str(uuid.uuid4())

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = base_key + self.key(*args, **kwargs)
            if self.memory.call_of(key) >= self.times:
                raise self.exception
            self.memory.inc_call(key, self.per)
            return func(*args, **kwargs)

        return wrapper

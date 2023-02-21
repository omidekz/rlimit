from pydantic import BaseModel
from typing import Callable, Union, ClassVar, Type
import functools
import uuid
from memory_abc import BaseMemory
from expiringdict_memory import ExpiringDictMemory


class BaseLimiter(BaseModel):
    """
        Usage
            @Limiter(times=10, per=10*Per.SECONDS)
    """
    times: int
    per: float
    key: Callable[[tuple, dict], str] = lambda *args, **kwargs: ''
    memory: ClassVar[BaseMemory] = ExpiringDictMemory()
    exception: ClassVar[Union[Type[BaseException], BaseException]] = OverflowError

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

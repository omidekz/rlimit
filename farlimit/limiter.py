import functools
from typing import Callable, ClassVar, Type, Union
from starlette.requests import Request
from starlette.exceptions import HTTPException
from per import Per
from memory import Memory


def identifier(request: Request):
    # TODO ** NAT PROBLEM !! **
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        ip = forwarded.split(",")[0]
    else:
        ip = request.client.host
    return f'{ip}:{request.method}:{request.scope["path"]}'


class Limiter(Per):
    """
        Usage
            @Limiter(times=10, per=10*Per.SECONDS)
    """
    times: int
    per: int
    memory: ClassVar[Type[Memory]] = Memory
    ex: Type[HTTPException] = HTTPException
    identifier: Callable[[Union[Request, dict]], str] = identifier
    key_maker: Callable[[dict], str] = lambda ka: ''
    request_parameter_name: str = 'request'
    message: str = "too many requests"

    @property
    def has_default_identifier(self):
        return self.identifier == identifier

    @classmethod
    def init(cls, memory=Memory):
        cls.memory = memory

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(**kwargs):
            embed_key = self.identifier(kwargs[self.request_parameter_name]) \
                        if self.has_default_identifier \
                        else self.identifier(kwargs)
            custom_key = self.key_maker(kwargs)
            key = f'{embed_key}:{custom_key}'
            times = self.memory.inc(key, ttl=self.per)
            if times > self.times:
                raise HTTPException(429, self.message)
            return func(**kwargs)
        return wrapper

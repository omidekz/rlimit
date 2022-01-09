import functools
from starlette.requests import Request
from per import Per
from memory import Memory
from typing import Callable, Optional, Type
from fastapi import HTTPException


def identifier(request: Request):
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
    memory: Type[Memory] = Memory
    ex: Type[HTTPException] = HTTPException
    identifier: Callable[[Request], str] = identifier
    key_maker: Optional[Callable[[Request, dict], str]]
    request_parameter_name: str = 'request'

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(**kwargs):
            req = kwargs.get(self.request_parameter_name)
            key = self.identifier(req) + ((':' + self.key_maker(req, kwargs)) if self.key_maker else '')
            times = self.memory.inc(key, ttl=self.per)
            if times > self.times:
                raise HTTPException(429)
            return func(**kwargs)
        return wrapper

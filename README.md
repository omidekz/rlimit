# FastAPIRateLimit

# Contributing is F&E (`free&easy`) [Y](#cneeds)
## Usage
    pip install farlimit
NOTE you have to define `starlette.requests.Request` as first argument

```py
from farlimit import Limiter
from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter(...)

@router.<any-method>(path)
@Limiter(times=3, per=5 * Limiter.SECONDS)
def test_ratelimit(request: Request):
    return 'no limit'
```
 - ### [Limiter Schema](https://github.com/omidekz/farlimit/blob/15cc5edd7e95fac84fefadbc3cee401a55086404/farlimit/limiter.py#L18) and options
 - ### if need to extend **Limiter** [Memory](https://github.com/omidekz/farlimit/blob/15cc5edd7e95fac84fefadbc3cee401a55086404/farlimit/memory.py#L5) (like on redis to distributed services)

# CNEEDS
  - RedisMemory
  - custom identifier
  - custom execption handler or callbacks
  - some api for reports
  - could we handle race condition?

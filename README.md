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


@router
```
 - ### [Limiter Description](./docs/limiter.md)

# CNEEDS
  - ~~RedisMemory~~
  - ~~custom identifier~~
  - custom execption handler or callbacks
  - some api for reports
  - could we handle race condition?

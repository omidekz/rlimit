# FastAPIRateLimit

## Usage
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

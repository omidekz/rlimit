# Rate Limit

this module help you to use rate limit in dev/production stage

\* NOTE in production we suggest use another type of `Memory` instead `expiring dict memory`

## Usage

`pip install git+https://github.com/omidekz/rlimit`

```py
from rlimit import Limiter
from fastapi import APIRouter, HTTPException

router = APIRouter(...)

@router.get(path)
@Limiter(times=3, per=5 * Limiter.SECOND, key=lambda r: r.client.host, exception=HTTPException)
def test_ratelimit(request: Request):
    return 'no limit'
```

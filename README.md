# Rate Limit

this package help you
to limit the call's `[frequent]` rates of any callable in python.

* default built-in memory is : [`expiring dict memory`](src/rlimit/expiringdict_memory.py)
  that not recommended for production usage

---

## Install

`pip install rlimit`

----

## Usage

#### basic usage

```py
from rlimit import Limiter, Per
from time import sleep


@Limiter(times=2, per=2 * Per.SECOND)
def func_a():
    return True


func_a()  # True
func_a()  # True
func_a()  # OverflowError
sleep(2)
func_a()  # True
func_a()  # True
func_a()  # OverflowError
```

---

#### key example

useful when uses in class or creating embed key

```py
from rlimit import Limiter, Per


@Limiter(
    times=2, per=2 * Per.SECOND,
    key=lambda name, age: str(hash((name, age)))
)
def func_a(name: str, age: int):
    return f'hi2{name}-{age}'


func_a('gzuz', 13)
func_a('gzuz', 14)
func_a('gzuz', 13)
func_a('gzuz', 15)
func_a('gzuz', 14)
func_a('gzuz', 14)  # OverflowError
func_a('gzuz', 13)  # OverflowError
```

---

#### key, exception

```py
from rlimit import Limiter, Per
from fastapi import APIRouter, HTTPException, Request

router = APIRouter(...)


@router.get(...)
@Limiter(
    times=2, per=4 * Per.SECOND,
    key=lambda r: r.client.host,
    exception=HTTPException(429)
)
def test_ratelimit(request: Request):
    return 'no limit'
```

----

## Custom Memory

to implement new memory class,
you have to extend [`BaseMemory`](src/rlimit/memory_abc.py) abstract class

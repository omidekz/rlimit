from base_limiter import BaseLimiter
from per import Per


class User:
    id: int
    name: str


# Limit the any call of func
@BaseLimiter(times=2, per=Per.SECOND * 3)
def hi1(name):
    return f'hello {name}'


# Limit the call of func based on key
@BaseLimiter(times=6, per=Per.MINUTE * 2, key=lambda u: u.id)
def hi2(user : User):
    return f'hello {user.name}'

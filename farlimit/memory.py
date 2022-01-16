from datetime import datetime as dt, timedelta
from errors import CoreInitException
from per import Per
from core_memory import Core


class Memory:
    core = Core()

    @classmethod
    def exists(cls, key: str):
        if cls.core is None:
            raise CoreInitException
        if not cls.core.get(key) \
            or dt.utcnow() >= cls.core.get(key)['until']:
            return False
        return True

    @classmethod
    def inc(cls, key: str, by: int = 1, ttl: int = None):
        """
        :ttl: int
            - default = 60 second
            - in milliseconds
            - ttl will set once if the key does not exist
        :by: int
            - default = 1
            - the logic is:
                SET(key, VALUE(key) + by)
        """
        if not cls.exists(key):
            val = {
                'count': 1,
                'until': dt.utcnow() + timedelta(milliseconds=ttl or 60 * Per.SECONDS)
            }
        else:
            val = cls.core.get(key)
            val['count'] += by
        cls.core.set(key, val)
        return val['count']

    @classmethod
    def value(cls, key: str):
        return cls.core.get(key, {}).get('count')


class RedisMemory:
    def __new__(cls, getter, setter):
        class tmp(Memory):
            core = Core(getter, setter)
        return tmp

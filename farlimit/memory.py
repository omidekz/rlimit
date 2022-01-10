from datetime import datetime as dt, timedelta
from .errors import CoreInitException


class Memory:
    core = dict()

    @classmethod
    def exists(cls, key: str):
        if cls.core is None:
            raise CoreInitException
        if key not in cls.core \
            or dt.utcnow() >= cls.core[key]['until']:
            return False
        return True

    @classmethod
    def inc(cls, key: str, by: int = 1, ttl: int = None):
        """
        :ttl: (int) in milliseconds
        """
        if not cls.exists(key):
            cls.core[key] = {
                'count': 0,
                'until': dt.utcnow() + timedelta(milliseconds=ttl)
            }
        cls.core[key]['count'] += by
        return cls.core[key]['count']

    @classmethod
    def value(cls, key: str):
        return cls.core.get(key, {}).get('count')

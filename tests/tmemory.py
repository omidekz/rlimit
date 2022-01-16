import unittest as ut
from limiter import Limiter
from memory import Memory, RedisMemory
from per import Per
import time


class MemoryTester(ut.TestCase):
    def test_exists(self):
        memory = Memory()
        key = 'a1'
        ttl = 3 * Per.SECONDS
        self.assertEqual(memory.exists(key), False)
        memory.inc(key, ttl=ttl)
        self.assertEqual(memory.exists(key), True)
        time.sleep(ttl // 1000)
        self.assertEqual(memory.exists(key), False)

    def test_value(self):
        memory = Memory()
        key = 'a2'
        memory.inc(key)


class RedisMemoryTester(ut.TestCase):
    def test_testm(self):
        data = dict()
        rm = RedisMemory(data.get, lambda k,v: data.update({k: v}))
        Limiter.init(rm)
        key = 'a1'
        self.assertEqual(Limiter.memory.value(key), None)
        Limiter.memory.inc(key, ttl=5 * Per.SECONDS)
        self.assertEqual(Limiter.memory.value(key), 1)
        Limiter.memory.inc(key, 2)
        self.assertEqual(Limiter.memory.value(key), 1 + 2)
        Limiter.memory.inc(key, 7)
        self.assertEqual(Limiter.memory.value(key), 1 + 2 + 7)


if __name__ == '__main__':
    ut.main()

import unittest as ut
from memory import Memory
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


if __name__ == '__main__':
    ut.main()

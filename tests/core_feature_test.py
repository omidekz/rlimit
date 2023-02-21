import uuid

from base_limiter import BaseLimiter
from per import Per
import unittest
from time import sleep


def func_a():
    return True


class CoreFeatureTest(unittest.TestCase):
    @staticmethod
    def new_wrapper(*, times: int = 2, per: float | int = Per.SECOND, **kwargs):
        return BaseLimiter(times=times, per=per, **kwargs)(func_a)

    def test_rate_limit_global_calls(self):
        wrapper = self.new_wrapper(times=2)
        self.assertTrue(wrapper())
        self.assertTrue(wrapper())
        self.assertRaises(OverflowError, wrapper)

    def test_rate_limit_global_calls_dispatch(self):
        wrapper = self.new_wrapper(times=2, per=2 * Per.SECOND)
        self.assertTrue(wrapper())
        self.assertTrue(wrapper())
        sleep(2)
        self.assertTrue(wrapper())
        self.assertTrue(wrapper())
        self.assertRaises(OverflowError, wrapper)

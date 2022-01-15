import unittest as ut
from per import Per


class PerTester(ut.TestCase):
    def test_per_second(self):
        ms = 1000
        ns = [1, 2, 4, .5]
        [self.assertEqual(n * Per.SECONDS, n * ms, f'{n} * Per.SECONDS != {n} * {ms}') for n in ns]

    def test_per_minute(self):
        ms = 1000 * 60
        ns = [1, 2, 4, .5]
        [self.assertEqual(n * Per.MINUTES, n * ms, f'{n} * Per.MINUTES != {n} * {ms}') for n in ns]

    def test_per_hour(self):
        ms = 1000 * 60 * 60
        ns = [1, 2, 4, .5]
        [self.assertEqual(n * Per.HOUR, n * ms, f'{n} * Per.HOUR != {n} * {ms}') for n in ns]

    def test_per_day(self):
        ms = 1000 * 60 * 60 * 24
        ns = [1, 2, 4, .5]
        [self.assertEqual(n * Per.DAY, n * ms, f'{n} * Per.DAY != {n} * {ms}') for n in ns]


if __name__ == '__main__':
    ut.main()

import enum
from typing import ClassVar


class Per(enum.IntEnum):
    SECOND: ClassVar[int] = 1
    MINUTE: ClassVar[int] = 60
    HOUR: ClassVar[int] = 60 * 60
    DAY: ClassVar[int] = 24 * 60 * 60

    def __mul__(self, other: int):
        return self.value * other

import enum
from typing import ClassVar


class Per:
    MILLISECOND: ClassVar[float] = .001
    SECOND: ClassVar[int] = 1
    MINUTE: ClassVar[int] = 60
    HOUR: ClassVar[int] = 60 * 60
    DAY: ClassVar[int] = 24 * 60 * 60

import enum

from pydantic import BaseModel
from typing import ClassVar


class Per(BaseModel):
    """
        Usage
        5 * Per.SECONDS
    """
    SECONDS: ClassVar[int] = 1000
    MINUTES: ClassVar[int] = 60 * 1000
    HOUR: ClassVar[int]    = 60 * 60 * 1000
    DAY: ClassVar[int]     = 24 * 60 * 60 * 1000

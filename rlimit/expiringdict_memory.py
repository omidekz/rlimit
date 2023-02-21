from typing import Dict, List
from time import time
from memory_abc import BaseMemory


class ExpiringDictMemory(BaseMemory):
    def __init__(self):
        self.data: Dict[str, List[float]] = dict()

    def inc_call(self, key: str, ttl: float):
        if not self.exists(key):
            self.data[key] = list()
        self.data[key].append(time() + ttl)

    def call_of(self, key: str) -> int:
        if not self.exists(key):
            return 0
        now, less_than_now_index, current_length = time(), 0, len(self.data[key])
        while less_than_now_index < current_length \
            and self.data[key][less_than_now_index] <= now:
            less_than_now_index += 1
        active_calls = len(self.data[key][less_than_now_index:])
        del self.data[key][:less_than_now_index]
        return active_calls

    def exists(self, key: str) -> bool:
        return key in self.data

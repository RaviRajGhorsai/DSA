from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        index = self.key_to_index(key)

        self.hashmap[index] = (key, value)

    def key_to_index(self, key: str) -> int:
        key_sum = sum(ord(k) for k in key)

        return key_sum % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def __repr__(self) -> str:
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

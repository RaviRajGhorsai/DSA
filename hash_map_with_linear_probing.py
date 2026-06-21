"""
Linear Probing
In the previous lessons, we've built a basic hash map that can add and retrieve key-value pairs. However, our current implementation does not handle collisions well. In the context of LockedIn, we want to make sure that user information can never be lost or overwritten.

Collisions happen when two different keys have the same index after applying the key_to_index function. To handle collisions, we can use a technique called linear probing.

Linear probing works by finding the next available slot after the collision index and placing the new key*value pair there.

"""

from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        index = self.key_to_index(key)

        original_index = index

        first_iteration = True

        while self.hashmap[index] is not None and key != self.hashmap[index][0]:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")

            index = (index + 1) % len(self.hashmap)

            first_iteration = False

        self.hashmap[index] = (key, value)

    def get(self, key: str) -> Any:
        index = self.key_to_index(key)

        original_index = index

        first_iteration = True

        while self.hashmap[index] is not None:
            if key == self.hashmap[index][0]:
                return self.hashmap[index][1]

            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")

            index = (index + 1) % len(self.hashmap)
            first_iteration = False

        raise Exception("sorry, key not found")

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

from typing import Any


class Trie:
    def add(self, word: str) -> None:
        curent_level = self.root

        for w in word:
            if w not in curent_level:
                curent_level[w] = {}

            curent_level = curent_level[w]

        curent_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"


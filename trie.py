from typing import Any


class Trie:
    def find_matches(self, document: str) -> set[str]:
        matches = set()

        for i in range(len(document)):
            current_level = self.root

            for j in range(i, len(document)):
                if document[j] not in current_level:
                    break
                current_level = current_level[document[j]]

                if self.end_symbol in current_level:
                    matches.add(document[i : j + 1])

        return matches

    def search_level(
        self, current_level: dict[str, Any], current_prefix: str, words: list[str]
    ) -> list[str]:
        if current_level is True:
            return words

        if self.end_symbol in current_level:
            words.append(current_prefix)

        for c in sorted(current_level.keys()):
            new_prefix = current_prefix + c

            words = self.search_level(current_level[c], new_prefix, words)

        return words

    def words_with_prefix(self, prefix: str) -> list[str]:

        current_level = self.root

        for c in prefix:
            if c not in current_level:
                return []
            else:
                current_level = current_level[c]

        return self.search_level(current_level, prefix, [])

    def exists(self, word: str) -> bool:
        current = self.root

        for w in word:
            if w not in current:
                return False

            current = current[w]

        if self.end_symbol in current:
            return True
        else:
            return False

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

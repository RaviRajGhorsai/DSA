from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.insert(0, item)

    def pop(self) -> Any:
        if len(self.items) == 0:
            raise ValueError("Queue is empty.")

        val = self.items[-1]

        del self.items[-1]

        return val

    def peek(self) -> Any:
        if len(self.items) == 0:
            raise ValueError("Queue is empty.")

        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def search_and_remove(self, item: Any) -> Any:
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self) -> str:
        return f"[{', '.join(self.items)}]"

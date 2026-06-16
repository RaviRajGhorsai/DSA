from node import Node


class LLQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def remove_from_head(self) -> Node | None:
        if self.head is None:
            return None

        removed = self.head

        self.head = removed.next

        if self.head is None:
            self.tail = None

        removed.next = None

        return removed 

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.set_next(node)

        self.tail = node

    # don't touch below this line

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

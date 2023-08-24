class Node:
    def __init__(self, value=None):
        self._value = value
        self._next: Node = None

    @property
    def value(self):
        return self._value

    @property
    def next(self) -> "Node":
        return self._next

    def set_next(self, node: "Node"):
        self._next = node

    def __eq__(self, other: "Node"):
        return other.value == self.value

    def __repr__(self):
        if self.next is None:
            next_node_str = "None"
        else:
            next_node_str = f"Node({self.next.value})"
        return f"Node({self._value}) -> {next_node_str}"
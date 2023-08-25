from src.linked_lists.node import Node


class LinkedList:
    def __init__(self):
        self._first: Node = None
        self._last: Node = None
        self._len = 0

    @property
    def first(self):
        return self._first

    def _empty(self):
        return self._first is None and self._last is None

    def add_first(self, node: Node):
        self._len += 1
        if self._empty():
            self._last = self._first = node
            return
        temp_first = self._first
        self._first = node
        self._first.set_next(temp_first)

    @property
    def last(self):
        return self._last

    def add_last(self, node: Node):
        self._len += 1
        if self._empty():
            self._first = self._last = node
            return
        self._last.set_next(node)
        self._last = node

    def __len__(self):
        return self._len

    def __bool__(self):
        return not self._empty()

    def remove_last(self):
        one_to_last = self.first
        for i in range(self._len):
            if one_to_last.next.next is None:
                break
            one_to_last = one_to_last.next
        self._last = one_to_last
        self._last.set_next(None)
        self._len -= 1

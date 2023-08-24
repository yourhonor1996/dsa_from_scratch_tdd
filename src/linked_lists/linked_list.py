from src.linked_lists.node import Node


class LinkedList:
    def __init__(self):
        self._first: Node = None
        self._last: Node = None

    @property
    def first(self):
        return self._first

    def _empty(self):
        return self._first is None and self._last is None

    def add_first(self, node: Node):
        if self._empty():
            self._last = self._first = node
            return
        temp_first = self._first
        self._first = node
        self._first.set_next(temp_first)
        # self._last =

    @property
    def last(self):
        return self._last

    def add_last(self, node: Node):
        if self._empty():
            self._first = self._last = node
            return
        self._last.set_next(node)
        self._last = node

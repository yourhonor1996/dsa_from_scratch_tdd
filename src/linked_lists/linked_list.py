from src.linked_lists.node import Node


class LinkedList:
    def __init__(self):
        self._first: Node = None
        self._last: Node = None
        self._len = 0

        self._iter_index = None
        self._iter_current: Node = None

    def __bool__(self):
        return not self.is_empty()

    def __len__(self):
        return self._len

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    def _insert_first_node(self, node):
        self._last = self._first = node
        self._iter_index = 0
        self._iter_current = self._first

    def _only_one_node_remains(self):
        return self._len == 1

    def _make_empty(self):
        self._len = 0
        self._first = self._last = None

    def is_empty(self):
        return self._first is None and self._last is None

    def add_first(self, node: Node):
        self._len += 1
        if self.is_empty():
            self._insert_first_node(node)
            return
        temp_first = self._first
        self._first = node
        self._first.set_next(temp_first)

    def add_last(self, node: Node):
        self._len += 1
        if self.is_empty():
            self._insert_first_node(node)
            return
        self._last.set_next(node)
        self._last = node

    def remove_first(self):
        temp_first = self._first
        if self._only_one_node_remains():
            self._make_empty()
            return temp_first
        second = self._first.next
        self._first = second
        self._len -= 1
        return temp_first

    def remove_last(self):
        temp_last = self._last
        if self._only_one_node_remains():
            self._make_empty()
            return temp_last

        one_to_last = self._first
        for i in range(self._len):
            if one_to_last.next.next is None:
                break
            one_to_last = one_to_last.next
        self._last = one_to_last
        self._last.set_next(None)
        self._len -= 1

        return temp_last

    # def __next__(self):
    #     self._it

    # def contains(self, param):
    #     value = param
    #     if isinstance(param, Node):
    #         value = param.value
    #     for i in range(self._len):

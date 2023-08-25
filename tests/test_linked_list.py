import pytest

from src.linked_lists.linked_list import LinkedList
from src.linked_lists.node import Node


class TestNode:
    def test_create_instance_without_data(self):
        node = Node()
        assert node

    def test_create_instance_with_data(self):
        node = Node(34)
        assert node.value == 34

    def test_if_created_empty_next_node_should_be_none(self):
        node = Node()
        assert node.next is None

    def test_if_created_with_value_next_node_should_be_none(self):
        node = Node(56)
        assert node.next is None

    def test_empty_node_representation(self):
        node = Node()
        assert str(node) == "Node(None) -> None"

    def test_a_node_with_value_but_no_next_not_repr(self):
        node = Node(34)
        assert str(node) == "Node(34) -> None"

    def test_set_next(self):
        node = Node(34)
        node.set_next(Node(45))

        assert node.next == Node(45)
        assert node.next.next is None

    def test_node_containing_next_node_repr(self):
        node = Node(45)
        node.set_next(Node(56))
        assert str(node) == "Node(45) -> Node(56)"


class TestLinkedList:
    @pytest.fixture
    def ll(self):
        return LinkedList()

    def test_is_empty(self, ll):
        assert not ll
        assert ll.is_empty() is True

    def test_null_linked_list_has_none_as_first_and_last_nodes(self, ll):
        assert ll.first is None
        assert ll.last is None

    def test_add_first_one_element(self, ll):
        ll.add_first(Node(43))
        assert ll.first == Node(43)

    def test_add_last_one_element(self, ll):
        ll.add_last(Node(56))
        assert ll.last == Node(56)

    def test_add_first_and_last_one_for_each(self, ll):
        ll.add_first(Node(43))
        ll.add_last(Node(78))
        assert ll.first == Node(43)
        assert ll.last == Node(78)

    def test_if_we_add_first_then_last_should_be_same_as_first(self, ll):
        ll.add_first(Node(45))
        assert ll.first == ll.last == Node(45)

    def test_if_we_add_last_then_first_should_be_same_as_last(self, ll):
        ll.add_last(Node(67))
        assert ll.first == ll.last == Node(67)

    def test_if_we_add_two_firsts(self, ll):
        ll.add_first(Node(1))
        ll.add_first(Node(2))
        assert ll.first == Node(2)
        assert ll.last == Node(1)
        assert ll.first.next == ll.last == Node(1)
        assert ll.last.next is None

    def test_if_we_add_two_lasts(self, ll):
        ll.add_last(Node(1))
        ll.add_last((Node(2)))

        assert ll.last == Node(2)
        assert ll.first == Node(1)
        assert ll.first.next == Node(2)
        assert ll.last.next is None

    def test_add_two_firsts_one_last(self, ll):
        ll.add_first(Node(2))
        ll.add_first(Node(1))
        ll.add_last(Node(3))
        assert ll.first == Node(1)
        assert ll.last == Node(3)
        assert ll.first.next == Node(2)
        assert ll.first.next.next == Node(3)
        assert ll.last.next is None

    def test_two_lasts_one_first(self, ll):
        ll.add_last(Node(1))
        ll.add_last(Node(2))
        ll.add_first(Node(-1))
        assert ll.first == Node(-1)
        assert ll.last == Node(2)
        assert ll.first.next == Node(1)
        assert ll.first.next.next == Node(2)
        assert ll.last.next is None
        return ll

    @pytest.fixture(name="full_ll")
    def create_linked_list_with_lots_of_data(self, ll) -> LinkedList:
        for i in range(20, 40):
            ll.add_last(Node(i))
        for i in reversed(range(20)):
            ll.add_first(Node(i))
        return ll

    def test_add_to_first_and_last_multiple(self, full_ll):
        next_one = full_ll.first
        for i in range(40):
            assert next_one == Node(i)
            next_one = next_one.next

    def test_len(self, full_ll):
        assert len(full_ll) == 40

    def test_remove_last(self, full_ll):
        node = full_ll.remove_last()
        assert node == Node(39)
        assert len(full_ll) == 39
        assert full_ll.last == Node(38)
        assert full_ll.last.next is None
        assert full_ll.first == Node(0)

        node = full_ll.remove_last()
        assert node == Node(38)

        assert len(full_ll) == 38
        assert full_ll.last == Node(37)
        assert full_ll.last.next is None
        assert full_ll.first == Node(0)

    def test_remove_first(self, full_ll):
        node = full_ll.remove_first()

        assert node == Node(0)
        assert len(full_ll) == 39
        assert full_ll.first == Node(1)
        assert full_ll.first.next == Node(2)
        assert full_ll.last == Node(39)

        node = full_ll.remove_first()

        assert node == Node(1)
        assert len(full_ll) == 38
        assert full_ll.first == Node(2)
        assert full_ll.first.next == Node(3)
        assert full_ll.last == Node(39)

    def test_remove_all_from_first(self, full_ll):
        for i in range(40):
            assert full_ll.remove_first() == Node(i)
            if len(full_ll) == 1:
                assert full_ll.first == full_ll.last == Node(39)
        assert full_ll.first is None and full_ll.last is None
        assert len(full_ll) == 0

    def test_remove_all_from_last(self, full_ll):
        for i in reversed(range(40)):
            assert full_ll.remove_last() == Node(i)
            if len(full_ll) == 1:
                assert full_ll.first == full_ll.last == Node(0)
        assert full_ll.first is None and full_ll.last is None
        assert len(full_ll) == 0

    # def test_remove

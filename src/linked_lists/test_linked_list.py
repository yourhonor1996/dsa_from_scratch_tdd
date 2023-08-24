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

    def test_create_instance(self, ll):
        assert ll

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

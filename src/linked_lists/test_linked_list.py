import pytest

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



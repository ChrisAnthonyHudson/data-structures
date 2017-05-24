"""Tests for stack class implementation."""

from stack import Stack
import pytest

EMPTY_LIST = Stack()
POP_LIST = Stack()
POP_LIST.push('one')
POP_LIST.push('two')
POP_LIST.push('three')
LIST_OF_THREE = Stack()
LIST_OF_THREE.push('one')
LIST_OF_THREE.push('two')
LIST_OF_THREE.push('three')
REMOVE_LIST = Stack()
REMOVE_LIST.push('orange')
REMOVE_LIST.push('apple')
REMOVE_LIST.push('grape')
LIST_LIST = Stack([1, 2, 3])
TUPLE_LIST = Stack((2, 4, 9))
STRING_LIST = Stack('cake')


def test_stack_pop_empty():
    """Test IndexError when pop method called on empty stack."""
    with pytest.raises(IndexError):
        EMPTY_LIST.pop()


def test_stack_push_none():
    """Test ValueError when push method called with arg of None."""
    with pytest.raises(ValueError):
        EMPTY_LIST.push(None)


def test_stack_push():
    """Test Stack push method with valid arg."""
    EMPTY_LIST.push(5)
    assert EMPTY_LIST._linked_list.head.val == 5


def test_stack_stack_not_iter():
    """Test IndexError when Stack instantiated with non-iterable."""
    with pytest.raises(TypeError):
        Stack(3)


def test_stack_push_mult():
    """Test confirm length of Stack when instantiated with an iterable arg."""
    assert len(LIST_LIST) == 3
    assert LIST_LIST._linked_list.head.val == 3
    assert len(TUPLE_LIST) == 3
    assert TUPLE_LIST._linked_list.head.val == 9
    assert len(STRING_LIST) == 4
    assert STRING_LIST._linked_list.head.val == 'e'


def test_stack_pop():
    """Test linked list pop method."""
    POP_LIST.pop()
    assert POP_LIST._linked_list.head.val == 'two'


def test_stack_len():
    """Test for len method."""
    assert len(LIST_OF_THREE) == 3
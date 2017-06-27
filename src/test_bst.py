"""Testing suite for Binary Search Tree data structure."""
import pytest
from bst import BST
from bst import Node


@pytest.fixture
def empty_bst():
    """Create empty BST."""
    return BST()


@pytest.fixture
def one_node_bst():
    """One node BST."""
    one_node = BST()
    one_node.insert(5)
    return one_node


@pytest.fixture
def three_node_bst():
    """A BST initialized with three nodes."""
    three_node = BST()
    three_node.insert(5)
    three_node.insert(23)
    three_node.insert(11)
    return three_node


@pytest.fixture
def three_node_bst_with_list():
    """A BST initialized with three nodes from list."""
    three_node = BST([2, 1, 3])
    return three_node


@pytest.fixture
def five_node_bst_with_tuple():
    """A BST initialized with five nodes from tuple."""
    five_node = BST((6, 4, 8, 7, 6.5))
    return five_node


@pytest.fixture
def five_node_bst_by_insert():
    """A BST initialized with five nodes from insert."""
    five_node = BST()
    five_node.insert(6)
    five_node.insert(2)
    five_node.insert(11)
    five_node.insert(4.2)
    five_node.insert(1)
    return five_node


@pytest.fixture
def five_node_edge_case():
    """A BST initialized with five nodes for edge case."""
    five_node = BST((6, 3, 2, 5, 4))
    return five_node


@pytest.fixture
def ten_node_bst_with_list():
    """A BST initialized with ten nodes from list."""
    ten_node = BST([10, 7, 12, 4, 9, 23, 2, 5, 17, 50])
    return ten_node


def test_empty_bst_features(empty_bst):
    """Test base features of empty BST."""
    assert empty_bst._root is None
    assert empty_bst._length == 0
    assert empty_bst._depth == 0
    assert empty_bst._balance == 0


def test_empty_bst_size_returns_0(empty_bst):
    """Test size of empty BST."""
    assert empty_bst.size() == 0


def test_empty_bst_depth_returns_0(empty_bst):
    """Test depth of empty BST."""
    assert empty_bst.depth() == 0


def test_empty_bst_balance_returns_0(empty_bst):
    """Test balance of empty BST."""
    assert empty_bst.balance() == 0


def test_init_with_int():
    """Test initalization of BST with an integer."""
    one_int = BST(10284)
    assert one_int.size() == 1
    assert one_int._root.val == 10284


def test_search_with_bad_data_type(one_node_bst):
    """Test bad data on search raises error."""
    with pytest.raises(TypeError):
        one_node_bst.search('five')


def test_contains_with_bad_data_type(one_node_bst):
    """Test bad data on contains raises error."""
    with pytest.raises(TypeError):
        one_node_bst.contains('lskdfj')


def test_repeat_val_insert_attempt_fails(one_node_bst):
    """Test that insert an exisiting val returns None."""
    assert one_node_bst.insert(5) is None


def test_one_node_bst_val_is_root(one_node_bst):
    """Test that a BST with one node has root of one node."""
    assert one_node_bst._root.val == 5


def test_one_node_bst_correct_size(one_node_bst):
    """Test that a BST with one node returns correct size."""
    assert one_node_bst.size() == 1


def test_one_node_bst_correct_balance(one_node_bst):
    """Test that one node BST returns balance of 0."""
    assert one_node_bst.balance() == 0


def test_one_node_bst_correct_depth(one_node_bst):
    """Test one node BST returns depth of 1."""
    assert one_node_bst.depth() == 1


def test_one_node_bst_search_returns_node(one_node_bst):
    """Test that one node BST search of one node's val returns root."""
    assert one_node_bst.search(5) == one_node_bst._root


def test_one_node_bst_contains_returns_true(one_node_bst):
    """Test one node BST contains val of one node."""
    assert one_node_bst.contains(5) is True


def test_one_node_bst_contains_returns_false(one_node_bst):
    """Test one node BST does not contain other value."""
    assert one_node_bst.contains(3145) is False


def test_three_node_bst_correct_size(three_node_bst):
    """Test that a three node BST returns 3."""
    assert three_node_bst.size() == 3


def test_three_node_bst_correct_balance(three_node_bst_with_list):
    """Test three node BST returns correct balance."""
    assert three_node_bst_with_list.balance() == 0


def test_three_node_bst_correct_depth(three_node_bst):
    """Test three node BST returns correct depth."""
    assert three_node_bst.depth() == 3


def test_three_node_bst_search_returns_node(three_node_bst_with_list):
    """Test three node BST search returns node searched for."""
    assert isinstance(three_node_bst_with_list.search(2), Node)
    assert three_node_bst_with_list.search(2).val == 2


def test_three_node_bst_contains_returns_true(three_node_bst):
    """Test three node BST contains two nodes that are in the BST."""
    assert three_node_bst.contains(5) is True
    assert three_node_bst.contains(23) is True


def test_three_node_bst_contains_returns_false(three_node_bst):
    """Test BST does returns false on bad node val."""
    assert three_node_bst.contains(3145) is False


def test_five_node_bst_correct_size(five_node_bst_with_tuple):
    """Test the size of a BST with 5 nodes."""
    assert five_node_bst_with_tuple.size() == 5


def test_five_node_bst_correct_balance(five_node_bst_by_insert):
    """Test the balance of a 5 node BST."""
    assert five_node_bst_by_insert.balance() == -1


def test_five_node_bst_correct_depth(five_node_bst_with_tuple):
    """Test the depth of a five node BST."""
    assert five_node_bst_with_tuple.depth() == 4


def test_five_node_bst_search_returns_node(five_node_bst_by_insert):
    """Test five node BST search returns node searched for."""
    assert isinstance(five_node_bst_by_insert.search(4.2), Node)
    assert five_node_bst_by_insert.search(4.2).val == 4.2


def test_five_node_bst_contains_returns_true(five_node_bst_with_tuple):
    """Test BST contains function of a five node BST."""
    assert five_node_bst_with_tuple.contains(6.5) is True
    assert five_node_bst_with_tuple.contains(4) is True


def test_five_node_bst_contains_returns_false(five_node_bst_by_insert):
    """Test bad contain function with val not in BST."""
    assert five_node_bst_by_insert.contains(3145) is False


def test_ten_node_bst_correct_size(ten_node_bst_with_list):
    """Test the size of a 10 node BST."""
    assert ten_node_bst_with_list.size() == 10


def test_ten_node_bst_correct_balance(ten_node_bst_with_list):
    """Test the balance of ten node BST."""
    assert ten_node_bst_with_list.balance() == 0


def test_ten_node_bst_correct_depth(ten_node_bst_with_list):
    """Test the depth of a 10 node BST."""
    assert ten_node_bst_with_list.depth() == 4


def test_init_bst_raises_type_error_with_dict():
    """Test init with dict raises TypeError."""
    with pytest.raises(TypeError):
        BST({4: 6, 5: 7, 3: 3})


def test_init_bst_raises_type_error_with_boolean():
    """Test init BST with boolean raises TypeError."""
    with pytest.raises(TypeError):
        BST(True)


def test_init_bst_raises_type_error_with_str():
    """Test init with str raises TypeError."""
    with pytest.raises(TypeError):
        BST('hiii')


def test_init_bst_raises_type_error_with_bad_data_in_list():
    """Test init with bad data in list raises TypeError."""
    with pytest.raises(TypeError):
        BST([4, '23', 'balls'])


def test_insert_with_bad_val_raises_type_error(one_node_bst):
    """Test insert with bad val raises TypeError."""
    with pytest.raises(TypeError):
        one_node_bst.insert('howdy')


def test_insert_with_list_raises_type_error(one_node_bst):
    """Test insert with list raises TypeError."""
    with pytest.raises(TypeError):
        one_node_bst.insert([23, 44])


def test_in_order_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses 'in order' order.
    """
    one = one_node_bst.in_order()
    assert next(one) == 5


def test_in_order_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses 'in order' order.
    """
    five = five_node_bst_with_tuple.in_order()
    assert next(five) == 4
    assert next(five) == 6
    assert next(five) == 6.5
    assert next(five) == 7
    assert next(five) == 8


def test_in_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'in order' order.
    """
    ten = ten_node_bst_with_list.in_order()
    assert next(ten) == 2
    assert next(ten) == 4
    assert next(ten) == 5
    assert next(ten) == 7
    assert next(ten) == 9
    assert next(ten) == 10
    assert next(ten) == 12
    assert next(ten) == 17
    assert next(ten) == 23
    assert next(ten) == 50


def test_pre_order_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses 'pre order' order.
    """
    one = one_node_bst.pre_order()
    assert next(one) == 5


def test_pre_order_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses 'pre order' order.
    """
    five = five_node_bst_with_tuple.pre_order()
    assert next(five) == 6
    assert next(five) == 4
    assert next(five) == 8
    assert next(five) == 7
    assert next(five) == 6.5


def test_pre_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'pre order' order.
    """
    ten = ten_node_bst_with_list.pre_order()
    assert next(ten) == 10
    assert next(ten) == 7
    assert next(ten) == 4
    assert next(ten) == 2
    assert next(ten) == 5
    assert next(ten) == 9
    assert next(ten) == 12
    assert next(ten) == 23
    assert next(ten) == 17
    assert next(ten) == 50


def test_post_order_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses 'post order' order.
    """
    one = one_node_bst.post_order()
    assert next(one) == 5


def test_post_order_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses 'post order' order.
    """
    five = five_node_bst_with_tuple.post_order()
    assert next(five) == 4
    assert next(five) == 6.5
    assert next(five) == 7
    assert next(five) == 8
    assert next(five) == 6


def test_post_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'post order' order.
    """
    ten = ten_node_bst_with_list.post_order()
    assert next(ten) == 2
    assert next(ten) == 5
    assert next(ten) == 4
    assert next(ten) == 9
    assert next(ten) == 7
    assert next(ten) == 17
    assert next(ten) == 50
    assert next(ten) == 23
    assert next(ten) == 12
    assert next(ten) == 10


def test_breadth_first_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses breadth first order.
    """
    one = one_node_bst.breadth_first()
    assert next(one) == 5


def test_breadth_first_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses breadth first order.
    """
    five = five_node_bst_with_tuple.breadth_first()
    assert next(five) == 6
    assert next(five) == 4
    assert next(five) == 8
    assert next(five) == 7
    assert next(five) == 6.5


def test_breadth_first_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses breadth first order.
    """
    ten = ten_node_bst_with_list.breadth_first()
    assert next(ten) == 10
    assert next(ten) == 7
    assert next(ten) == 12
    assert next(ten) == 4
    assert next(ten) == 9
    assert next(ten) == 23
    assert next(ten) == 2
    assert next(ten) == 5
    assert next(ten) == 17
    assert next(ten) == 50


def test_post_order_edge_case(five_node_edge_case):
    """Test to left child of right child bubble up edge case."""
    five = five_node_edge_case.post_order()
    assert next(five) == 2
    assert next(five) == 4
    assert next(five) == 5
    assert next(five) == 3
    assert next(five) == 6


def test_on_empty_bst_delete_returns_None(empty_bst):
    assert empty_bst.delete(7) is None


def test_bad_data_delete_raises_error(empty_bst):
    with pytest.raises(TypeError):
        empty_bst.delete('lkj')


def test_delete_of_root_on_one_node_bst(one_node_bst):
    one_node_bst.delete(5)
    assert one_node_bst._root is None


def test_delete_of_root_on_two_node_bst():
    new_bst = BST([2, 5])
    new_bst.delete(2)
    assert new_bst._root.val == 5
    assert new_bst._length == 1
    assert new_bst.balance() == 0
    assert new_bst.depth() == 1


def test_delete_on_five_node_bst_with_tuple(five_node_bst_with_tuple):
    """Test delete functionality on a five node BST once."""
    five_node = five_node_bst_with_tuple
    five_node.delete(8)
    assert five_node._root.right.val == 7
    assert five_node.balance() == 1
    assert five_node.depth() == 3


def test_delete_head_on_five_node_bst_with_insert(five_node_bst_by_insert):
    five_node_bst_by_insert.delete(6)
    assert five_node_bst_by_insert._root.val == 4.2


def test_delete_multiple_heads_on_five_node_bst(five_node_bst_by_insert):
    five_node_bst_by_insert.delete(6)
    assert five_node_bst_by_insert._root.val == 4.2
    assert five_node_bst_by_insert.depth() == 3
    five_node_bst_by_insert.delete(4.2)
    assert five_node_bst_by_insert._root.val == 2
    assert five_node_bst_by_insert.depth() == 2


def test_ten_node_delete_2_nodes(ten_node_bst_with_list):
    ten_node_bst_with_list.delete(9)
    assert ten_node_bst_with_list._length == 9
    ten_node_bst_with_list.delete(10)
    assert ten_node_bst_with_list._root.val == 7
    node7 = ten_node_bst_with_list.search(7)
    assert node7.right.val == 12
    assert node7.parent is None


def test_ten_node_delete_right_side(ten_node_bst_with_list):
    ten_node_bst_with_list.delete(23)
    assert ten_node_bst_with_list._root.right.right.val == 17








# =========================================ELY TESTS DO NOT USE=========
#
#
#     def test_delete_node_empty_returns_none(bst_empty):
#     """Test delete with empty bst."""
#     assert bst_empty.delete(5) is None
#
#
# def test_delete_on_empty_bst_leaves_bst_intact(bst_empty):
#     """Pretty verbose test name."""
#     bst_empty.delete(1)
#     assert bst_empty._root is None
#
#
# def test_delete_tree_with_one_node_leaves_empty_tree(bst_empty):
#     """Delete single node."""
#     bst_empty.insert(1)
#     assert bst_empty.delete(1) is None
#     with pytest.raises(AttributeError):
#         bst_empty._root.val
#     assert bst_empty.size() == 0
#
#
# def test_delete_two_node_left_balanced_tree_01(bst_empty):
#     """Delete root node shifts other node."""
#     bst_empty.insert(2)
#     bst_empty.insert(1)
#     bst_empty.delete(2)
#     assert bst_empty._root.val == 1
#     assert bst_empty._root.left is None
#
#
# def test_delete_two_node_left_balanced_tree_02(bst_empty):
#     """Delete last node leaves one node tree."""
#     bst_empty.insert(2)
#     bst_empty.insert(1)
#     bst_empty.delete(1)
#     assert bst_empty._root.val == 2
#     assert bst_empty._root.right is None
#     assert bst_empty._root.left is None
#     # assert len(bst_empty) == 1
#
#
# def test_delete_left_tree_single_child(bst_left_balance):
#     """One child deletion test."""
#     bst_left_balance.delete(4)
#     assert bst_left_balance.search(3).val == 3
#     assert bst_left_balance.search(4) is None
#
#
# def test_delete_two_node_right_balanced_tree_01(bst_empty):
#     """Delete root node shifts other node."""
#     bst_empty.insert(1)
#     bst_empty.insert(3)
#     bst_empty.delete(1)
#     assert bst_empty._root.val == 3
#     assert bst_empty._root.left is None
#
#
# def test_delete_two_node_right_balanced_tree_02(bst_empty):
#     """Delete last node leaves one node tree."""
#     bst_empty.insert(1)
#     bst_empty.insert(3)
#     bst_empty.delete(3)
#     assert bst_empty._root.val == 1
#     assert bst_empty._root.right is None
#     assert bst_empty._root.left is None
#     assert len(bst_empty) == 1
#
#
# def test_delete_three_node_tree_01(three):
#     """Delete route node leaves tree in correct order."""
#     three.delete(2)
#     assert three._root.val == 3
#     assert three._root.right is None
#     assert three._root.left.val == 1
#     assert tuple(three.in_order()) == (1, 3)
#
#
# def test_delete_three_node_tree_02(three):
#     """Delete left node leaves tree in order."""
#     three.delete(1)
#     assert three._root.val == 2
#     assert three._root.right.val == 3
#     assert three._root.left is None
#     assert tuple(three.in_order()) == (2, 3)
#
#
# def test_delete_three_node_tree_03(three):
#     """Delete right node leaves tree in order."""
#     three.delete(3)
#     assert three._root.val == 2
#     assert three._root.right is None
#     assert three._root.left.val == 1
#     assert tuple(three.in_order()) == (1, 2)
#
#
# def test_delete_complex_tree_01(comp):
#     """Delete route 10."""
#     comp.delete(10)
#     assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 11, 12, 13, 14, 15)
#     assert tuple(comp.breadth_first()) == (11, 6, 13, 4, 8, 12, 14, 7, 9, 15)
#
#
# def test_delete_complex_tree_02(comp):
#     """Delete left most 4."""
#     comp.delete(4)
#     assert tuple(comp.in_order()) == (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
#     assert tuple(comp.breadth_first()) == (10, 6, 13, 8, 11, 14, 7, 9, 12, 15)
#
#
# def test_delete_complex_tree_03(comp):
#     """Delete right most 15."""
#     comp.delete(15)
#     assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 12, 13, 14)
#     assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 11, 14, 7, 9, 12)
#
#
# def test_delete_complex_tree_04(comp):
#     """Delete mid right 13."""
#     comp.delete(13)
#     assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 12, 14, 15)
#     assert tuple(comp.breadth_first()) == (10, 6, 14, 4, 8, 11, 15, 7, 9, 12)
#
#
# def test_delete_complex_tree_05(comp):
#     """Delete mid left 8."""
#     comp.delete(8)
#     assert tuple(comp.in_order()) == (4, 6, 7, 9, 10, 11, 12, 13, 14, 15)
#     assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 9, 11, 14, 7, 12, 15)
#
#
# def test_delete_complex_tree_06(comp):
#     """Delete bottom left 9."""
#     comp.delete(9)
#     assert tuple(comp.in_order()) == (4, 6, 7, 8, 10, 11, 12, 13, 14, 15)
#     assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 11, 14, 7, 12, 15)
#
#
# def test_delete_complex_tree_07(comp):
#     """Delete bottom right 12."""
#     comp.delete(12)
#     assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 13, 14, 15)
#     assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 11, 14, 7, 9, 15)
#
#
# def test_delete_complex_tree_08(comp):
#     """Delete mid bottom right 11."""
#     comp.delete(11)
#     assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 12, 13, 14, 15)
#     assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 12, 14, 7, 9, 15)

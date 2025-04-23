import pytest
from collections.abc import MutableMapping
from project.tree.cartesian_tree import Treap


@pytest.fixture
def treap():
    tree = Treap()
    data = {3: "c", 1: "a", 2: "b", 4: "d"}
    for k, v in data.items():
        tree[k] = v
    return tree


def test_get_set(treap):
    assert treap[1] == "a"
    assert treap[2] == "b"
    treap[1] = "z"
    assert treap[1] == "z"


def test_len(treap):
    assert len(treap) == 4
    treap[5] = "e"
    assert len(treap) == 5
    del treap[3]
    assert len(treap) == 4


def test_in_operator(treap):
    assert 1 in treap
    assert 99 not in treap


def test_delete(treap):
    del treap[2]
    assert 2 not in treap
    with pytest.raises(KeyError):
        _ = treap[2]


def test_iteration_order(treap):
    assert list(treap) == [1, 2, 3, 4]


def test_reversed_iteration(treap):
    assert list(reversed(treap)) == [4, 3, 2, 1]


def test_items_keys_values(treap):
    items = list(treap.items())
    keys = list(treap.keys())
    values = list(treap.values())

    assert items == list(zip(keys, values))
    assert keys == [1, 2, 3, 4]
    assert set(values) == {"a", "b", "c", "d"}


def test_repr(treap):
    s = repr(treap)
    for k, v in [(1, "a"), (2, "b"), (3, "c"), (4, "d")]:
        assert f"{k}: {v}" in s


def test_update_existing_value(treap):
    old_len = len(treap)
    treap[1] = "updated"
    assert treap[1] == "updated"
    assert len(treap) == old_len


def test_key_error(treap):
    with pytest.raises(KeyError):
        _ = treap[999]
    with pytest.raises(KeyError):
        del treap[999]


def test_is_instance_mutablemapping(treap):
    assert isinstance(treap, MutableMapping)

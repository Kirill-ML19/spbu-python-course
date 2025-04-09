import pytest
from collections.abc import MutableMapping
from project.cartesian_three.cartesian_three import Treap


@pytest.fixture
def treap():
    tree = Treap()
    data = {"c": 3, "a": 1, "b": 2, "d": 4}
    for k, v in data.items():
        tree[k] = v
    return tree


def test_get_set(treap):
    assert treap["a"] == 1
    assert treap["b"] == 2
    treap["a"] = 10
    assert treap["a"] == 10


def test_len(treap):
    assert len(treap) == 4
    treap["e"] = 5
    assert len(treap) == 5
    del treap["c"]
    assert len(treap) == 4


def test_in_operator(treap):
    assert "a" in treap
    assert "z" not in treap


def test_delete(treap):
    del treap["b"]
    assert "b" not in treap
    with pytest.raises(KeyError):
        _ = treap["b"]


def test_iteration_order(treap):
    assert list(treap) == ["a", "b", "c", "d"]


def test_reversed_iteration(treap):
    assert list(reversed(treap)) == ["d", "c", "b", "a"]


def test_items_keys_values(treap):
    items = list(treap.items())
    keys = list(treap.keys())
    values = list(treap.values())

    assert items == list(zip(keys, values))
    assert keys == ["a", "b", "c", "d"]
    assert set(values) == {1, 2, 3, 4}


def test_repr(treap):
    s = repr(treap)
    for k, v in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
        assert f"{k}: {v}" in s


def test_update_existing_value(treap):
    old_len = len(treap)
    treap["a"] = 999
    assert treap["a"] == 999
    assert len(treap) == old_len


def test_key_error(treap):
    with pytest.raises(KeyError):
        _ = treap["x"]
    with pytest.raises(KeyError):
        del treap["x"]


def test_is_instance_mutablemapping(treap):
    assert isinstance(treap, MutableMapping)

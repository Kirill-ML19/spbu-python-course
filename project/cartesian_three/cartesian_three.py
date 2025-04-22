import random
from collections.abc import MutableMapping
from typing import Optional, Iterator, Tuple, Any, ItemsView, KeysView, ValuesView


class TreapNode:
    """Node of a Cartesian Tree (Treap).

    Attributes:
        key (int): The key of the node.
        value (Any): The value associated with the key.
        priority (float): Randomly assigned priority (heap property).
        left (Optional[TreapNode]): Left child.
        right (Optional[TreapNode]): Right child.
    """

    def __init__(self, key: int, value: Any, priority: Optional[float] = None):
        """Initializes a treap node."""
        self.key: int = key
        self.value: Any = value
        self.priority: float = priority if priority is not None else random.random()
        self.left: Optional["TreapNode"] = None
        self.right: Optional["TreapNode"] = None

    def __repr__(self) -> str:
        """String representation of the node."""
        return f"({self.key}: {self.value}, prio={self.priority:.2f})"


def split(
    root: Optional[TreapNode], key: int
) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
    """Splits a tree into two parts: <= key and > key."""
    if root is None:
        return (None, None)
    elif key < root.key:
        left, right = split(root.left, key)
        root.left = right
        return (left, root)
    else:
        left, right = split(root.right, key)
        root.right = left
        return (root, right)


def merge(left: Optional[TreapNode], right: Optional[TreapNode]) -> Optional[TreapNode]:
    """Merges two treaps into one, preserving heap and BST properties."""
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right


class Treap(MutableMapping):
    """Treap (Cartesian Tree) implementing the MutableMapping interface.

    Supports dict-like behavior with additional heap property for balancing.
    """

    def __init__(self):
        """Initializes an empty treap."""
        self.root: Optional[TreapNode] = None
        self._size: int = 0

    def __setitem__(self, key: int, value: Any) -> None:
        """Inserts or updates a key-value pair in the treap."""
        if key in self:
            self._replace(self.root, key, value)
        else:
            self.root = self._insert(self.root, TreapNode(key, value))
            self._size += 1

    def _insert(
        self, root: Optional[TreapNode], node: TreapNode
    ) -> Optional[TreapNode]:
        """Recursively inserts a node into the tree."""
        if root is None:
            return node
        if node.key < root.key:
            root.left = self._insert(root.left, node)
            if root.left and root.left.priority > root.priority:
                root = self._rotate_right(root)
        else:
            root.right = self._insert(root.right, node)
            if root.right and root.right.priority > root.priority:
                root = self._rotate_left(root)
        return root

    def _rotate_right(self, root: TreapNode) -> TreapNode:
        """Performs right rotation."""
        left = root.left
        assert left is not None
        root.left = left.right
        left.right = root
        return left

    def _rotate_left(self, root: TreapNode) -> TreapNode:
        """Performs left rotation."""
        right = root.right
        assert right is not None
        root.right = right.left
        right.left = root
        return right

    def _replace(self, root: Optional[TreapNode], key: int, value: Any) -> None:
        """Recursively replaces value by key."""
        if root is None:
            return
        if key < root.key:
            self._replace(root.left, key, value)
        elif key > root.key:
            self._replace(root.right, key, value)
        else:
            root.value = value

    def __getitem__(self, key: int) -> Any:
        """Retrieves the value associated with the key."""
        node = self._get_node(self.root, key)
        if node is None:
            raise KeyError(key)
        return node.value

    def _get_node(self, root: Optional[TreapNode], key: int) -> Optional[TreapNode]:
        """Finds and returns the node with the given key."""
        if root is None:
            return None
        if key < root.key:
            return self._get_node(root.left, key)
        elif key > root.key:
            return self._get_node(root.right, key)
        else:
            return root

    def __delitem__(self, key: int) -> None:
        """Deletes the element with the given key."""
        if key not in self:
            raise KeyError(key)
        self.root = self._delete(self.root, key)
        self._size -= 1

    def _delete(self, root: Optional[TreapNode], key: int) -> Optional[TreapNode]:
        """Recursively deletes a node from the tree."""
        if root is None:
            return None
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            root = merge(root.left, root.right)
        return root

    def __contains__(self, key: object) -> bool:
        """Checks whether the key exists in the tree."""
        if not isinstance(key, int):
            return False
        return self._get_node(self.root, key) is not None

    def __len__(self) -> int:
        """Returns the number of elements in the tree."""
        return self._size

    def __iter__(self) -> Iterator[int]:
        """Returns an in-order iterator over the keys."""
        yield from self._inorder(self.root)

    def _inorder(self, root: Optional[TreapNode]) -> Iterator[int]:
        """In-order traversal generator."""
        if root:
            yield from self._inorder(root.left)
            yield root.key
            yield from self._inorder(root.right)

    def __reversed__(self) -> Iterator[int]:
        """Returns a reversed in-order iterator over the keys."""
        yield from self._reversed_inorder(self.root)

    def _reversed_inorder(self, root: Optional[TreapNode]) -> Iterator[int]:
        """Reverse in-order traversal generator."""
        if root:
            yield from self._reversed_inorder(root.right)
            yield root.key
            yield from self._reversed_inorder(root.left)

    def items(self) -> ItemsView[int, Any]:
        """Returns a view of (key, value) pairs."""
        return ItemsView(self)

    def _items(self, root: Optional[TreapNode]) -> Iterator[Tuple[int, Any]]:
        """Generator for (key, value) pairs in in-order."""
        if root:
            yield from self._items(root.left)
            yield (root.key, root.value)
            yield from self._items(root.right)

    def keys(self) -> KeysView[int]:
        """Returns a view of keys in the tree."""
        return KeysView(self)

    def values(self) -> ValuesView[Any]:
        """Returns a view of values in the tree."""
        return ValuesView(self)

    def __repr__(self) -> str:
        """Returns a string representation of the treap."""
        return "{" + ", ".join(f"{k}: {v}" for k, v in self._items(self.root)) + "}"

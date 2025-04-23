import random
from collections.abc import MutableMapping


class TreapNode:
    """
    Cartesian tree node.

    Attributes:
    key: The node's key.
    value: The value associated with the key.
    priority: The node's priority for maintaining the heap (random by default).
    left: The left child.
    right: The right child.
    """

    def __init__(self, key, value, priority=None):
        self.key = key
        self.value = value
        self.priority = priority if priority is not None else random.random()
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.key}: {self.value}, prio={self.priority:.2f})"


def split(root, key):
    """
    Splits the tree into two by key.
    """
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


def merge(left, right):
    """
    Combines two Cartesian trees.
    """
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right


class Treap(MutableMapping):
    """
    Cartesian tree is a data structure with a mapping interface (dict-like).

    Implements the MutableMapping interface:
    - Access and modification by key.
    - Delete by key.
    - Check for presence.
    - Forward and reverse iterator.
    """

    def __init__(self):
        """
        Creates an empty Cartesian tree.
        """
        self.root = None
        self._size = 0

    def __setitem__(self, key, value):
        """
        Adds or updates an element by key.
        """
        if self.__contains__(key):
            self._replace(self.root, key, value)
        else:
            self.root = self._insert(self.root, TreapNode(key, value))
            self._size += 1

    def _insert(self, root, node):
        """
        Inserts a node into the tree.
        """
        if root is None:
            return node
        if node.key < root.key:
            root.left = self._insert(root.left, node)
            if root.left.priority > root.priority:
                root = self._rotate_right(root)
        else:
            root.right = self._insert(root.right, node)
            if root.right.priority > root.priority:
                root = self._rotate_left(root)
        return root

    def _rotate_right(self, root):
        """
        Right turn of the tree.
        """
        left = root.left
        root.left = left.right
        left.right = root
        return left

    def _rotate_left(self, root):
        """
        Left turn of the tree.
        """
        right = root.right
        root.right = right.left
        right.left = root
        return right

    def _replace(self, root, key, value):
        """
        Replaces the value by key.
        """
        if root is None:
            return
        if key < root.key:
            self._replace(root.left, key, value)
        elif key > root.key:
            self._replace(root.right, key, value)
        else:
            root.value = value

    def __getitem__(self, key):
        """
        Returns the value by key.
        """
        node = self._get_node(self.root, key)
        if node is None:
            raise KeyError(key)
        return node.value

    def _get_node(self, root, key):
        """
        Returns a node by key (or None).
        """
        if root is None:
            return None
        if key < root.key:
            return self._get_node(root.left, key)
        elif key > root.key:
            return self._get_node(root.right, key)
        else:
            return root

    def __delitem__(self, key):
        """
        Removes an element by key.
        """
        if not self.__contains__(key):
            raise KeyError(key)
        self.root = self._delete(self.root, key)
        self._size -= 1

    def _delete(self, root, key):
        """
        Removes a node from the tree.
        """
        if root is None:
            return None
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            root = merge(root.left, root.right)
        return root

    def __contains__(self, key):
        """
        Checks if a key exists in a tree.
        """
        return self._get_node(self.root, key) is not None

    def __len__(self):
        """
        Returns the number of elements in the tree.
        """
        return self._size

    def __iter__(self):
        """
        Returns a forward iterator over the keys (in-order).
        """
        yield from self._inorder(self.root)

    def _inorder(self, root):
        """
        Direct bypass.
        """
        if root:
            yield from self._inorder(root.left)
            yield root.key
            yield from self._inorder(root.right)

    def __reversed__(self):
        """
        Returns a reversed in-order iterator over the keys.
        """
        yield from self._reversed_inorder(self.root)

    def _reversed_inorder(self, root):
        """
        Reverse bypass.
        """
        if root:
            yield from self._reversed_inorder(root.right)
            yield root.key
            yield from self._reversed_inorder(root.left)

    def items(self):
        """
        Returns an iterator over (key, value) pairs.
        """
        yield from self._items(self.root)

    def _items(self, root):
        if root:
            yield from self._items(root.left)
            yield (root.key, root.value)
            yield from self._items(root.right)

    def keys(self):
        """
        Returns an iterator over keys.
        """
        return iter(self)

    def values(self):
        """
        Returns an iterator over values.
        """
        for _, value in self.items():
            yield value

    def __repr__(self):
        """
        String representation of a tree.
        """
        return "{" + ", ".join(f"{k}: {v}" for k, v in self.items()) + "}"

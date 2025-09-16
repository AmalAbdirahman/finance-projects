from Node import Node
from TreePrinter import print_tree

class TreeNode:

    """A node in a binary tree, storing a key and value with references to children and parent.

        Attributes:
            _key: The key stored in the node (e.g., a timestamp).
            _value: The value associated with the key (e.g., price data).
            _left (TreeNode or None): The left child node.
            _right (TreeNode or None): The right child node.
            _parent (TreeNode or None): The parent node.
        """
    def __init__(self, key=None,value=None, left=None, right=None, parent=None):
        """Initializes a TreeNode with the given key, value, and references.

        Args:
            key: The key for the node (default: None).
            value: The value associated with the key (default: None).
            left (TreeNode or None): The left child node (default: None).
            right (TreeNode or None): The right child node (default: None).
            parent (TreeNode or None): The parent node (default: None).
        """
        self._key = key
        self._left = left
        self._right = right
        self._parent = parent
        self._value = value

        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if parent is not None:
            self.parent = parent



    @property
    def key(self):
        """The value of the node."""
        return self._key

    @key.setter
    def key(self,value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    @property
    def left(self):
        """The left child of this node."""
        return self._left

    @left.setter
    def left(self, value):
        if value is not None and not isinstance(value, TreeNode):
            raise TypeError("Left child must be TreeNode or None")
        if self._left is not None:
            self._left._parent = None
        self._left = value
        if value:
            value.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        if value is not None and not isinstance(value, TreeNode):
            raise TypeError("Right child must be TreeNode or None")
        if self._right is not None:
            self._right._parent = None
        self._right = value
        if value:
            value.parent = self

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def depth(self):
        depth = 1
        current = self.parent
        while current:
            depth += 1
            current = current.parent
        return depth


    def remove_leaf(self,n):
        """Removes a leaf node if it is a child of this node.

        Args:
            n (TreeNode): The node to remove.

        Returns:
            TreeNode: The removed leaf node.

        Raises:
            TypeError: If n is not a TreeNode.
            ValueError: If n is not a leaf node or not a child of this node.
        """
        if not isinstance(n,TreeNode):
            raise TypeError
        if self.left == n:
            if n.left is None and n.right is None:
                self.left = None
                return n
        if self.right == n:
            if n.left is None and n.right is None:
                self.right = None
                return n
            else:
                raise ValueError
        raise ValueError


    def __repr__(self):
        return f"Key:{self.key},Left: {self.left}, Right:{self.right}, Parent:{self.parent}"












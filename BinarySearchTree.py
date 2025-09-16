from TreeNode import TreeNode
from BST import BST

class BinarySearchTree(BST):
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, value=None):
        new_node = TreeNode(key, value)
        if self.root is None:
            # (a) Tree is empty
            self.root = new_node
        else:
            current = self.root
            while True:
                if key == current.key:
                    # (b) Node with given key is already present
                    current.value = value
                    break
                elif key < current.key:
                    if current.left is None:
                        # (c) Insert new node as left child
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        # (c) Insert new node as right child
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        raise KeyError(f"Key {key} not found in the tree")

    def get_value(self, key):
        node = self.search(key)
        return node.value

    def delete(self, key):
        def delete_node(node, key):
            if node is None:
                raise ValueError(f"Key {key} not found in the tree")
            if key < node.key:
                node.left = delete_node(node.left, key)
            elif key > node.key:
                node.right = delete_node(node.right, key)
            else:
                # Node with the key found
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    # Node with two children
                    successor = self._get_min(node.right)
                    node.key, node.value = successor.key, successor.value
                    node.right = delete_node(node.right, successor.key)
            return node

        self.root = delete_node(self.root, key)

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def range_query(self, low, high):
        def range_query_recursive(node, low, high, result):
            if node is not None:
                if low < node.key:
                    range_query_recursive(node.left, low, high, result)
                if low <= node.key <= high:
                    result.append((node.key, node.value))
                if high > node.key:
                    range_query_recursive(node.right, low, high, result)
            return result

        return range_query_recursive(self.root, low, high, [])







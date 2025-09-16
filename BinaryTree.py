from TreeNode import TreeNode

def inorder(node):
    if node is None:
        return []
    result = inorder(node.left)
    result += [node.key]
    result += inorder(node.right)
    return result

def preorder(node):
    if node is None:
        return []
    result = [node.key]
    result += preorder(node.left)
    result += preorder(node.right)
    return result

def postorder(node):
    if node is None:
        return []

    result = postorder(node.left)
    result += postorder(node.right)
    result += [node.key]
    return result

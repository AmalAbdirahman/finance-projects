from TreeNode import TreeNode
from BinaryTree import inorder, preorder, postorder

tree1= TreeNode(10)
tree1.left = TreeNode(5)
tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(8)
tree1.right = TreeNode(15)
tree1.right.left = TreeNode(12)
tree1.right.left = TreeNode(18)

tree2 = TreeNode("a")
tree2.left = TreeNode("b")
tree2.left.left = TreeNode("z")
tree2.right = TreeNode("axe")

tree3 = TreeNode(3)
tree3.left = TreeNode(17)
tree3.left.right = TreeNode(4)
tree3.left.right.right = TreeNode(5)
tree3.right = TreeNode(23)
tree3.right.right = TreeNode(-1)


for tree, name in zip([tree1, tree2, tree3], ['\ntree1', '\ntree2', '\ntree3']):
    print(f"{name} Inorder: {inorder(tree)}")
    print(f"{name} Preorder: {preorder(tree)}")
    print(f"{name} Postorder: {postorder(tree)}")
    print(f"{name} Root Representation: {tree.__repr__()}")
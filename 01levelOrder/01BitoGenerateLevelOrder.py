# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历二叉树
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# 中序遍历二叉树
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# 后序遍历二叉树
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# 主函数
if __name__ == '__main__':
    # 创建一个二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 前序遍历二叉树
    print('前序遍历二叉树：')
    preorder(root)

    # 中序遍历二叉树
    print('中序遍历二叉树：')
    inorder(root)

    # 后序遍历二叉树
    print('后序遍历二叉树：')
    postorder(root)
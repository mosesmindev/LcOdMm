from collections import deque

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#def findBottomLeftValue(self,root:Optional[TreeNode]) -> int:
def findBottomLeftValue(root) -> int:
    if root == None:
        return []
    ans = root.val
    q = deque()
    q.append(root)
    while q:
        qSize = len(q)
        ans = q[0].val
        for _ in range(qSize):
            node = q.popleft()
            if node.left != None:
                q.append(node.left)

            if (node.right!= None):
                q.append(node.right)
    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    result = findBottomLeftValue(root)

    # 打印结果
    print(result)

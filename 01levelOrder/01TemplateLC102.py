from collections import deque

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root) -> list[list[int]]:
    # if root is None:
    # if root == None:
    if not root:
        return []
    ans = list()
    q = deque()
    q.append(root)

    # while len(q) > 0:
    # while len(q):
    while q:
        qSize = len(q)
        sublist = list()
        for _ in range(qSize):
            node = q.popleft()
            sublist.append(node.val)
            # if node.left != None:
            if node.left:
                q.append(node.left)
            # if node.right != None:
            if node.right:
                q.append(node.right)
        ans.append(sublist)
    return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    result = levelOrder(root)
    print(result)



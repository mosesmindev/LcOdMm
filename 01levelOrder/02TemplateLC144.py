
class TreeNode:
    def __init__(self,val = '', left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
# def preOrderTraversal(root):
#     ans = list()
#     traversal(ans,root)
#     return ans
# def traversal(ans,node):
#     if not node:
#         print("return")
#         return
#     ans.append(node.val)
#     print("1-ans:", str(ans),", node.val:",str(node.val))
#     traversal(ans,node.left)
#     print("2-ans:", str(ans))
#     if node.left:
#         print("2-ans:", str(ans),", node.left.val:",str(node.left.val))
#     traversal(ans,node.right)
#     print("3-ans:", str(ans))
#     if node.right:
#         print("3-ans:", str(ans), ", node.right.val:", str(node.right.val))
#     print("#######################################")


def preOrderTraversal(root):
    ans = list()
    traversal(ans,root)
    return ans


def traversal(ans,node):
    if not node:
        return
    ans.append(node.val)
    traversal(ans,node.left)
    traversal(ans, node.right)


if __name__ == '__main__':
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    result = preOrderTraversal(root)
    print(result)



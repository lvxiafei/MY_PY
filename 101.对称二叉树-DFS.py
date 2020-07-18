'''
递归：
    拆分小规模
    出口条件

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(node):  # dfs
    def helper(root,mirror):
        if not root and not mirror:
            return True
        if root and mirror and root.val == mirror.val:
            return helper(root.left, mirror.right) and helper(root.right,mirror.left)
        return False
    return helper(node.left, node.right)


'''
bfs使用一个队列
在队列中同时取出两个节点left,right,判断这两个节点的值是否相等，然后把他们的孩子按照
（left,left,right,right）一组，（left,right,right.left）一组放入队中，

'''
def isSymmetric2(root): # bfs
    import collections
    queue = collections.deque()
    # print(queue)
    queue.append((root, root))
    while queue:
        left, right = queue.popleft()
        if not left and not right: continue
        if not left or not right: return False
        if left.val != right.val:
            return False
        queue.append((left.left,right.right))
        queue.append((left.right,right.left))
    return True

if __name__ == '__main__':
     root = TreeNode(1)
     root.right = TreeNode(2)
     root.left = TreeNode(2)
     root.left.left = TreeNode(3)
     root.left.right = TreeNode(4)
     root.right.right = TreeNode(3)
     root.right.left = TreeNode(4)
     print(isSymmetric2(root))
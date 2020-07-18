
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归
# def inorderTraversal(root: TreeNode):
#     res = []
#     def helper(root): # 左 中 右
#         if not root: return
#         helper(root.left) # 假设较小的规模已完成
#         res.append(root.val)
#         helper(root.right)
#     helper(root)
#     return res

# 模仿递归
def inorderTraversal(root: TreeNode):
    res = [] # 结果列表，结构存储
    stack =[] # 辅助栈，执行顺序
    cur = root # 当前节点
    while cur or stack:
        while cur : # 遍历到最后一层
            stack.append(cur)
            cur = cur .left
        top = stack.pop() # 此时左子树遍历完成
        res.append(top.val) # 将父节点加入列表
        cur = top.right # 遍历右子树
    return res



if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(inorderTraversal(root))
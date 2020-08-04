'''
输入判断
1. 二叉树生成
2. 子树翻转输出

思路2：
    位置关系：用一维数组进行操作，通过数学关系确定位置，重新赋值即可

'''


# 定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 输入
# n, m = map(int,input().split())
# print(n,m)
n, m = 4 ,3
# 生成完全二叉树，列表转二叉树
l = list(range(1,2**n))
# print(l)


def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)


# binary_tree = list_to_binarytree([3, 9, 20, None, None, 15, 7])
binary_tree = list_to_binarytree(l)



# 二叉树转列表、输出
def print_in_one_line(root):
    ''' 1. 简单版： 打印在一行内，不换行 '''
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end = " ") # end属性默认为“\n”，所以print()函数默认会换行。此处设为空格“ ”，防止自动换行
        if node.left:
            queue.append(node.left) # 将本节点的左子节点入队
        if node.right:
            queue.append(node.right) # 将本节点的右子节点入队
    # print()
# print_in_one_line(print_in_one_line(binary_tree))

# 找到该节点
def findNode(root,key):
    if not root:    return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if node.val == key: return node
        if node.left:
            queue.append(node.left)  # 将本节点的左子节点入队
        if node.right:
            queue.append(node.right)  # 将本节点的右子节点入队

f = findNode(binary_tree,m)
# print(f.val)

# 子树翻转
def invertTree(root):
    if not root:
        return None
    root.left, root.right=invertTree(root.right),invertTree(root.left)
    return root

ret = invertTree(f)
# print_in_one_line(ret)
print_in_one_line(binary_tree)
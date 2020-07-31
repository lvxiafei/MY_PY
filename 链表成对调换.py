# 链表成对调换
# 1->2->3->4转换成2->1->4->3.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
冷静分析：
    分治
        先交换前两个，后面的递归调用

'''
def swapPairs(head):  # 从后向前连
    if head != None and head.next != None:
        next = head.next # 保存第二个节点，作为交换的第一个节点

        head.next = swapPairs(next.next)  # 指向第三个元素 赋给 head.next

        next.next = head   # 第一个节点此时作为第二个节点

        # head.next, next.next = swapPairs(next.next), head

        return next  # 第二个节点此时作为第一个节点
    return head

def output(head):
    while head != None:
        print(head.val, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    output(root)

    output(swapPairs(root))

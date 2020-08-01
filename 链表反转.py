

class Node:
    data = 0
    next = None

# 数组转链表
def build_single_link_list(nodeArr):
    head_node = None  # 头节点
    next_node = None  # 临时节点，存储已生成的最后一个节点，指向新生成的节点
    for i in nodeArr:
        node = Node()
        node.data = i
        node.next = None
        '''
        思维顺序：
            生成第一个节点赋给头节点，并把头节点赋给临时节点 head/node(1)
            临时节点指向新生成的节点，新生成的节点赋给临时节点 head/node(1)->node(2)->...
        '''
        if head_node is None: # 生成第一个节点
            head_node = node  # 如果头节点为空，把新生成的节点给头节点
            next_node = head_node  # 生成节点
        else:
        # elif next_node is not None:  # 如果临时节点不为空
            next_node.next = node  # 如果头节点不为空(临时节点不为空)，把新生成的元素加到后面
            # next_node = node
            next_node = next_node.next  # 后移

    return head_node

# 链表转数据输出
def output(head):
    ret = []
    while head is not None:
        ret.append(head.data)
        # print(head.data)
        head = head.next
    return ret

# 算法1（非递归实现）：使用3个指针，分别指向前序结点、当前结点和后序结点，
# 遍历链表，逐个逆转，时间复杂度O(n)：
def reverse1(head):
    if head is None or head.next is None:  # 链表为空 或 单节点
        return head
    current = head
    pre = None
    pnext = None
    '''
    此处的思维顺序是什么：
        
    '''
    while current is not None:
        pnext = current.next
        current.next = pre
        pre = current
        current = pnext

    return pre

# 算法2（递归实现）： 不断逆转当前结点，直到链表尾端，时间复杂度O(n)：
def reverse2(current):
    if current.next is None:
        return current
    pnext = current.next
    current.next = None
    reversed = reverse2(pnext)
    pnext.next = current

    return reversed

# 算法3（递归实现）：和算法2类似，不过递归传入当前结点和前序结点，代码可读性要好点，时间复杂度O(n)：
def reverse3(current, pre):
    if current.next is None:
        current.next = pre
        return current
    else:
        pnext = current.next
        current.next = pre
        return reverse3(pnext, current)


if __name__ == '__main__':
    head = build_single_link_list([1, 2, 3, 4, 5])
    print("原链表", output(head))
    head = reverse1(head)
    print("impl1:", output(head))
    # while head is not None:
    #     print(head.data)
    #     head = head.next

    print("impl2:")
    head = build_single_link_list([1, 2, 3, 4, 5])
    head = reverse2(head)
    while head is not None:
        print(head.data, end = ' ')
        head = head.next
    print("\nimpl3:")
    head = build_single_link_list([1, 2, 3, 4, 5])
    head = reverse3(head,None)
    while head is not None:
        print(head.data, end = ' ')
        head = head.next


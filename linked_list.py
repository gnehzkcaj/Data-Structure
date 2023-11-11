class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用

def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


def find(head: ListNode, target: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    P.next = n1
    n0.next = P

def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1


# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
# 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
p  = ListNode(9)
# 构建引用指向
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Example usage:
target_value = 5

# Find the index of the node with the target value in the linked list
index = find(n0, target_value)

# Check if the value was found in the list
if index != -1:
    print(f"Node with value {target_value} found at index {index}.")
else:
    print(f"Node with value {target_value} not found in the linked list.")


print(n3.val)
print(n3.next.val)
print(n1.next.next.val)
print(n3)

insert(n0, p)

print(n0.next.val)

print(n3.next.val)

remove(n2)

print(n2.next.val)

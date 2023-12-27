# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
    
    def swapPairs2(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = dummy = ListNode(-1)
        dummy.next = head
        while cur.next is not None and cur.next.next is not None:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
       
        return dummy.next;
        
        
# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Create an instance of the Solution class
solution_instance = Solution()

# Call the swapPairs method on the linked list
swap_list_head = solution_instance.swapPairs2(a)

# Print the swaped Linked List
while swap_list_head:
    print(swap_list_head.val, end=" ")
    swap_list_head = swap_list_head.next

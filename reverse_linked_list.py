# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """       
        if not head or not head.next:
            return head

        new_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_list

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create an instance of the Solution class
solution_instance = Solution()

# Reverse the linked list
reversed_list_head = solution_instance.reverseList(a)

# Print the reversed linked list
while reversed_list_head:
    print(reversed_list_head.val, end=" ")
    reversed_list_head = reversed_list_head.next




        
     
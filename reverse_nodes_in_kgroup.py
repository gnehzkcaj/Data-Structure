# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# https://www.youtube.com/watch?v=1UOPsfP85V4
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
        
            prev, curr = kth.next, groupPrev.next
        
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
                                        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
               
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create an instance of the Solution class
solution_instance = Solution()

# Reverse the linked list
reversed_list_head = solution_instance.reverseKGroup(a, 2)

# Print the reversed linked list
while reversed_list_head:
    print(reversed_list_head.val, end=" ")
    reversed_list_head = reversed_list_head.next
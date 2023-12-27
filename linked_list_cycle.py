# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.findIndex(head, slow)
        return None

    def findIndex(self, head, meeting_point):
        index = 0
        ptr1 = head
        ptr2 = meeting_point

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            index += 1

        return ptr1
        # return index

a = Solution()
  
list1 = ListNode(3)
list1.next = ListNode(2)
list1.next.next = ListNode(0)
list1.next.next.next = ListNode(-4)
list1.next.next.next.next = list1.next

list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = list2

list3 = ListNode(1)

print(a.hasCycle(list1))
print(a.hasCycle(list2))
print(a.hasCycle(list3))

print(a.detectCycle(list1))
print(a.detectCycle(list2))
print(a.detectCycle(list3))


























        

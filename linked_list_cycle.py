# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while (slow is not fast):
            if slow.next is None:
                return False
            slow = slow.next 
            if fast.next is None or fast.next.next is None:
                return False 
            fast = fast.next.next
        return True


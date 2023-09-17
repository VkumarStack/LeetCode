# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        curr = head
        nxt = head.next
        head.next = None 
        while (nxt is not None):
            tmp = nxt.next
            nxt.next = curr 
            curr = nxt
            nxt = tmp
        return curr

test = Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        h = []
        for node in lists:
            if node is not None:
                # heapq resorts to comparing the other values of the tuple if there are duplicates, and LeetCode 
                # doesn't let me override the __lt__ method, so I have the next value be the object id of each node (which
                # shouldn't duplicate) so that it never directly compares the nodes but stills lets me access them
                heapq.heappush(h, (node.val, id(node), node))
        
        if len(h) == 0:
            return None
        
        node = heapq.heappop(h)[2]
        if node.next is not None:
            heapq.heappush(h, (node.next.val, id(node), node.next))
        head = node
        current = head 
        
        while len(h) != 0:
            node = heapq.heappop(h)[2]
            if node.next is not None:
                heapq.heappush(h, (node.next.val, id(node), node.next))
            current.next = node
            current = current.next
        
        current.next = None
        return head 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = ListNode(0, head)

        node = head
        prev = sentinel
        i = 0
        while node:
            if i < m:
                prev.next = node
                prev = node
            i += 1
            i %= (m+n)    
            node = node.next
        prev.next = None
        return sentinel.next

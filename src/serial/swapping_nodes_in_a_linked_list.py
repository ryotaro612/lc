# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        if n == 1:
            return head
        
        node1 = head
        for i in range(k-1):
            node1 =node1.next
        node2 = head
        for i in range(n-k):
            node2 = node2.next

        node1.val, node2.val = node2.val, node1.val
        return head

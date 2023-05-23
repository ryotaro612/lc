# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        if n == 1:
            return None

        node = head
        for _ in range(n // 2 - 1):
            node = node.next
        node.next = node.next.next

        return head

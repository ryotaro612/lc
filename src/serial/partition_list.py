# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first_sentinel = first = ListNode()
        second_sentinel = second = ListNode()

        node = head
        while node:
            if node.val < x:
                first.next = node
                first = first.next
            else:
                second.next = node
                second = second.next
            node = node.next
        first.next = second.next = None
        first.next = second_sentinel.next
        
        return first_sentinel.next

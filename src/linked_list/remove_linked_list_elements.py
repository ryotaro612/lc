# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        
        node = head
        prev = sentinel
        while node:
            if node.val != val:
                prev.next = node
                prev = node
            node = node.next
        prev.next = None
        return sentinel.next
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        
        while True:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            slow = slow.next
            if fast is slow:
                break
                
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return slow

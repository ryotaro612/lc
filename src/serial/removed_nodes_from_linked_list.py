# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'))
        cur = head
        stack = [dummy]
        while cur:
            while stack[-1].val < cur.val:
                stack.pop()
            stack[-1].next = cur
            stack.append(cur)
            cur = cur.next
        
        return dummy.next

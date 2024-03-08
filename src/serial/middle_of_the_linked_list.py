# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n+=1
        
        mid = n // 2
        
        result = head
        for _ in range(mid):
            result = result.next
        return result 

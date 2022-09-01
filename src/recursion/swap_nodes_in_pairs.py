# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        result = head.next
        
        p1, p2 = head, head.next
        while True:
            temp = p2.next
            p2.next = p1
            if temp is None:
                p1.next = None
                break
            elif temp.next is None:
                p1.next = temp
                break
            else:
                p1.next = temp.next
            
            p1 = temp
            p2 = p1.next
        return result

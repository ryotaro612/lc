# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        node = head
        while node:
            if node.val:
                cur.val += node.val
            else:
                cur.next = ListNode()
                cur = cur.next

            node = node.next
        
        cur = dummy.next
        while cur.next:
            if cur.next.val == 0:
                cur.next = None
                break
            cur = cur.next
        return dummy.next

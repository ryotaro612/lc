# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
        
#         subseq = self.swapPairs(head.next.next)
#         node = head.next
#         head.next = subseq
#         node.next = head
#         return node
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        node = head
        head = head.next
        prev = None
        
        while node is not None:
            if node.next is None:
                prev.next = node
                break
            else:
                forward = node.next
                backward = node
                backward.next = node.next.next
                forward.next = backward
                if prev:
                    prev.next = forward
                prev = backward
                node = backward.next
                
        return head
                    

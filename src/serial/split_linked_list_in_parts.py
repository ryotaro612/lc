# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        prev = ListNode(0, head)
        node = head
        result = []

        for i in range(k):
            if node:
                result.append(node)
                for _ in range(n // k + (i < (n-n//k*k))):
                    prev = node
                    node = node.next
                prev.next = None
            else:
                result.append(None)
        
        return result

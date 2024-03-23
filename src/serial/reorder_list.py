# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        sentinel = ListNode()
        node = sentinel

        i = -1
        j = len(nodes)
        while i < j:
            i += 1
            if i < j:
                node.next = nodes[i]
                node = node.next
            j -= 1
            if i < j:
                node.next = nodes[j]
                node = node.next
        
        node.next = None
        return sentinel.next


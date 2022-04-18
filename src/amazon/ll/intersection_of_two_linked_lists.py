# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
8
[4,1,8,4,5]
[5,6,1,8,4,5]
2
3

0
[2,6,4]
[1,5]
3
2

0
[2,6,4]
[1,5]
3
2
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = self.countNodes(headA)
        len_b = self.countNodes(headB)
        nodeA = headA
        nodeB = headB
        
        if len_a < len_b:
            nodeB = self.forward(headB, len_b - len_a)
        elif len_b < len_a:
            nodeA = self.forward(headA, len_a - len_b)
        
        while nodeA is not None and nodeB is not None:
            if nodeA is nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            
        return None
    
    def countNodes(self, head: ListNode) -> int:
        node  = head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count
    
    def forward(self, head: ListNode, times: int):
        node = head
        for _ in range(times):
            node = node.next
        return node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1 2 3 4 5
[1] 2 [5] 4 3
1 5 2 4 3

1 2 3 4 5 6
[1] 2 3 [6] 5 4
1 6 2 5 3 4
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        
        n = self.computeLength(head)
        mid_node = head
        for i in range(n // 2):
            mid_node = mid_node.next
    
        head2 = self.reverseList(mid_node)
        # 1 2 3 4
        # 1 2 4 3
        node, node2 = head, head2
        for i in range(n // 2):
            temp, temp2 = node.next, node2.next
            print(node.val, node2.val)
            node.next = node2
            node = temp
            if i < n // 2 - 1:
                node2.next = node
                node2 = temp2
            else:
                if n % 2 == 0:
                    node2.next = None
                
                    
        # self.debug(head)
    
    def computeLength(self, head):
        node = head
        i = 0
        while node is not None:
            node = node.next
            i+= 1
        return i
    
    def debug(self, head):
        a = head
        while a is not None:
            print(a.val)
            a = a.next
        
    def reverseList(self, head):
        """
        1 -> 2 -> 3
        1 <- 2 <- 3
        1 -> 2 -> 3 -> 4
        1 <- 2 <- 3 <- 4
        """
        if head is None:
            return None
        
        node = head
        next_node = head.next
        while True:
            if next_node is None:
                head.next = None
                return node
            temp = next_node.next
            next_node.next = node
            node = next_node
            next_node = temp
    
        

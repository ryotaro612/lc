# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
[1,2,5,3,9,2,1]
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        n = self.count_len(head)
        
        if n % 2 == 0:
            head2_pos = n // 2
        else:
            head2_pos = n // 2 + 1
        head2 = head
        for _ in range(head2_pos):
            head2 = head2.next
        tail1_pos = n // 2 - 1
        tail = head
        for _ in range(tail1_pos):
            tail = tail.next
        tail.next = None
        
        head = self.reverse(head)
        
        while head:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
    
        
    def reverse(self, head):
        if head.next is None:
            return head
        node1, node2 = head, head.next
        head.next = None
        
        while node2 is not None:
            next_node = node2.next
            node2.next = node1
            node1 = node2
            node2 = next_node
        return node1
    
    def count_len(self, head):
        res = 0
        while head:
            head = head.next
            res += 1
        return res    

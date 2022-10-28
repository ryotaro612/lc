# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = self.countLen(head)
        for i in range(1, n):
            node = head
            prev = None
            for _ in range(i):
                prev = node
                node = node.next
            
            if node.val < prev.val:
                prev.next = node.next
                peek = head
                prev = None                
                while peek and peek.val < node.val:
                    prev = peek
                    peek = prev.next
                
                if prev:        
                    node.next = prev.next
                    prev.next = node
                else:
                    node.next = head
                    head = node
        return head
    
    def countLen(self, head):    
        result = 0
        while head:
            result += 1
            head = head.next
            
        return result
    
    
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        sentinel = ListNode(0, head)
        rev_head = head
        prev = sentinel
        for _ in range(left-1):
            prev = rev_head
            rev_head = rev_head.next
        
        tail = rev_head
        for i in range(right - left):
            tail = tail.next
        
        third_head = tail.next
        tail.next = None
        # rev_head -> 2
        # tail -> 4
        # prev -> 1
        # third_head -> 5

        # revese [rev_head,,,tail]
        node = rev_head
        peek = node.next
        node.next = None
        while peek:
            temp = peek.next
            peek.next = node
            node = peek
            peek = temp
        
        prev.next = tail
        rev_head.next = third_head
        return sentinel.next

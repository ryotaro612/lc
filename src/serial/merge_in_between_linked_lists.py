# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        a-1th
        b+1th node
        """
        node = ListNode(0, list1)
        for i in range(b+1):
            node = node.next
            if i == a-1:
                prev_a = node
            if i == b:
                next_b = node.next
        
        prev_a.next = list2
        node = list2
        while node.next != None:
            node = node.next
        
        node.next = next_b
        return list1

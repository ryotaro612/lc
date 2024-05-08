# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        
        double = []
        carry = 0
        for num in nums[::-1]:
            num = 2 * num + carry
            double.append(num % 10)
            carry = num // 10
        if carry:
            double.append(carry)
        
        double.reverse()

        dummy = ListNode()
        node = dummy
        for v in double:
            node.next = ListNode(v)
            node = node.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        dummy = ListNode()
        cursor = dummy
        node = head
        while node:
            if node.val not in nums:
                cursor.next = node
                cursor = node
            node = node.next
        
        cursor.next = None
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.build_tree(0, len(arr), arr)

    def build_tree(self, left, right, arr) -> TreeNode:
        if right <= left:
            return None
        pivot = (left + right) // 2

        node = TreeNode(arr[pivot])

        node.left = self.build_tree(left, pivot, arr)
        node.right = self.build_tree(pivot+1, right, arr)
        return node  

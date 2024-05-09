# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None

        node =TreeNode(max(nums))
        for i in range(len(nums)):
            if nums[i] == node.val:
                node.left = self.constructMaximumBinaryTree(nums[:i])
                node.right = self.constructMaximumBinaryTree(nums[i+1:])
                return node
        

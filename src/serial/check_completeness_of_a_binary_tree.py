"""
[1,2,3,5,null,7]
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        found = False

        que = deque([root])
        while que:
            node = que.popleft()
            if node is None:
                found = True
            else:
                if found:
                    return False
                que.append(node.left)
                que.append(node.right)
        return True


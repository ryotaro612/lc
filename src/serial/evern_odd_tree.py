from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev_depth = -1
        prev_val = 0
        que = deque([[root, 0]])
        
        while que:
            node, depth = que.popleft()
            if depth % 2 and node.val % 2 or depth % 2 == 0 and node.val % 2 == 0:
                return False
                
            if prev_depth == depth:
                if depth % 2:
                    if not prev_val > node.val:
                        return False
                else:
                    if not prev_val < node.val:
                        return False
            else:
                prev_depth = depth
            prev_val = node.val
            for child in [node.left, node.right]:
                if child:
                    que.append([child, depth+1])

        return True

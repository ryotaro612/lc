from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre = deque(preorder)
        post = deque(postorder)

        return self.rec(pre, post)

    def rec(self, pre, post):
        if len(pre) == 0:
            return
        
        val = pre.popleft()
        node = TreeNode(val)
        if post[0] == val:
            post.popleft()
            return node
        node.left = self.rec(pre, post)

        if post[0] == val:
            post.popleft()
            return node
        
        node.right = self.rec(pre, post)
        post.popleft()
        return node

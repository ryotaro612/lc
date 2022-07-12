# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        mini = []
        que = deque()
        que.append(root)
        while len(que) > 0:
            node = que.popleft()
            mini.append(node.val)
            mini = list(set(mini))
            mini.sort()
            mini = mini[:2]
            if node.left:
                que.append(node.left)
                que.append(node.right)
        if len(mini) == 2:
            return mini[1]
        else:?
            return -1

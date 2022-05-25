# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        vertical = dict()
        que = deque()
        que.append((root, 0))
        while len(que) > 0:
            node, pos = que.popleft()
            if node is None:
                continue
            if pos not in vertical:
                vertical[pos] = []
            vertical[pos].append(node.val)
            que.append((node.left, pos-1))
            que.append((node.right, pos+1))
            
        mini, maxi = 10000, -10000
        for pos in vertical.keys():
            mini = min(mini, pos)
            maxi = max(maxi, pos)
            
        result = [[] for _ in range(maxi - mini + 1)]
        offset = abs(mini)
        
        for pos in vertical.keys():
            result[pos + offset] = vertical[pos]
        return result
        

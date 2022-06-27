"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.split(0, 0, len(grid), grid)
    
    def split(self, r, c, n, grid):
        
        if 1 == len({grid[i][j] for j in range(c, c+n) for i in range(r, r+n)}):
            return Node(grid[r][c] == 1, True, None, None, None, None)
        
        next_n = n // 2
        top_left = self.split(r, c, next_n, grid)
        top_right = self.split(r, c+next_n, next_n, grid)
        bottom_left = self.split(r+next_n, c, next_n, grid)
        bottom_right = self.split(r+next_n, c+next_n, next_n, grid)
        
        return Node(True, False, top_left, top_right, bottom_left, bottom_right)

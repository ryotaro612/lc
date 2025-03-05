class Solution:
    def coloredCells(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 5
        
        cross = (n-1) * 4 + 1
        triangle = (n-2) * (n-1) // 2 * 4
        return cross + triangle

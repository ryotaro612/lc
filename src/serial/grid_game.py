class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum1 = sum(grid[0])
        sum2 = 0

        result = float('inf')
        n = len(grid[0])
        for c in range(n):
            sum1 -= grid[0][c]
            if c:
                sum2 += grid[1][c-1]
            result = min(result, max(sum1, sum2))
        return result    

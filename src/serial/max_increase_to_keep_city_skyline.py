
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        board = [[float('inf')] * n for _ in range(n)]

        north = [0] * n
        for c in range(n):
            for r in range(n):
                north[c] = max(north[c], grid[r][c])

        west = [0] * n
        for r in range(n):
            for c in range(n):
                west[r] = max(west[r], grid[r][c])

        result = 0
        for r in range(n):
            for c in range(n):
                board[r][c] = min(board[r][c], north[c], west[r])
                result += board[r][c] - grid[r][c]
        
        return result



class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0
        
        up = [[0] * n for _ in range(n)]
        for c in range(n):
            for r in range(n):
                if grid[r][c]:
                    if r:
                        up[r][c] += 1 + up[r-1][c]
                    else:
                        up[r][c] = 1
        down = [[0] * n for _ in range(n)]
        for c in range(n):
            for r in range(n-1, -1, -1):
                if grid[r][c]:
                    if r == n-1:
                        down[r][c] = 1
                    else:
                        down[r][c] += 1 + down[r+1][c]
        left = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    if c:
                        left[r][c] += 1 + left[r][c-1]
                    else:
                        left[r][c] = 1
        
        right = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n-1, -1, -1):
                if grid[r][c]:
                    if c == n - 1:
                        right[r][c] = 1
                    else:
                        right[r][c] += 1 + right[r][c+1]
        
        result = 0
        for r in range(n):
            for c in range(n):
                result = max(result, min(up[r][c], down[r][c], left[r][c], right[r][c]))
        
        return result

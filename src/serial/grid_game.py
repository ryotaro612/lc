class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_sum=[[0] * (n + 1) for _ in range(2)]
        for r in range(2):
            for c in range(n):
                prefix_sum[r][c+1] = grid[r][c] + prefix_sum[r][c]

        for c in range(n):
            if c == 0:
                result = prefix_sum[0][n] - prefix_sum[0][1]
            elif c == n - 1:
                result = min(result, prefix_sum[1][n-1])
            else:
                result = min(result, max(prefix_sum[1][c], prefix_sum[0][n] - prefix_sum[0][c+1]))

        return result

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        r, c = 0, 0
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        j = 0
        for i in range(1, n*n+1):
            grid[r][c] = i
            n_r = r + delta[j][0]
            n_c = c + delta[j][1]
            if 0 <= n_r < n and 0 <= n_c < n and grid[n_r][n_c] == 0:
                r, c = n_r, n_c
            else:
                j += 1 
                j %= 4
                r += delta[j][0]
                c += delta[j][1]
        return grid

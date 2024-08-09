class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        result = 0
        for r in range(n_rows-2):
            for c in range(n_cols - 2):
                sub_grid = [[0] * 3 for _ in range(3)]
                digits = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        sub_grid[i-r][j-c] = grid[i][j]
                        digits.add(grid[i][j])
                sum_patterns = set()
                for i in range(3):
                    sum_patterns.add(sum(sub_grid[i][:3]))
                sum_patterns.add(sub_grid[0][0] + sub_grid[1][1] + sub_grid[2][2])
                sum_patterns.add(sub_grid[0][2] + sub_grid[1][1] + sub_grid[2][0])
                sum_patterns.add(sub_grid[0][0] + sub_grid[1][0] + sub_grid[2][0])
                sum_patterns.add(sub_grid[0][1] + sub_grid[1][1] + sub_grid[2][1])
                sum_patterns.add(sub_grid[0][2] + sub_grid[1][2] + sub_grid[2][2])
                # print(r, c, sum_patterns)
                if len(sum_patterns) == 1 and len([d for d in digits if 0 < d < 10]) == 9:

                    result += 1
        return result

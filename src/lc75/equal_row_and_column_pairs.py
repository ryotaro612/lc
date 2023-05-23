from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = Counter([tuple(row) for row in grid])

        result = 0
        n = len(grid)

        for i in range(n):
            result += freq[tuple([grid[r][i] for r in range(n)])]

        return result

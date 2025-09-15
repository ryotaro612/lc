class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """
        upper 2 lower 1 col
        """
        n = len(colsum)
        grid = [[0] * n for _ in range(2)]

        for i in range(n):
            if colsum[i] == 0:
                continue
            elif colsum[i] == 1:
                if max(upper, lower) == 0:
                    return []
                if upper > lower:
                    upper -= 1
                    grid[0][i] = 1
                else:
                    lower -= 1
                    grid[1][i] = 1
            elif upper > 0 and lower > 0:
                upper -= 1
                lower -= 1
                grid[0][i] = grid[1][i] = 1
                continue
            else:
                return []
        if upper == 0 and lower == 0:
            return grid
        return []

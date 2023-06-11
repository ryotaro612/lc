from collections import defaultdict


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n_row, n_col = len(picture), len(picture[0])
        row_pos, col_pos = defaultdict(int), defaultdict(int)
        for r in range(n_row):
            for c in range(n_col):
                if picture[r][c] == "B":
                    row_pos[r] += 1
                    col_pos[c] += 1

        result = 0
        for r in range(n_row):
            for c in range(n_col):
                if picture[r][c] == "B" and row_pos[r] == 1 and col_pos[c] == 1:
                    result += 1
        return result

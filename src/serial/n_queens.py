import itertools
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        for perm in itertools.permutations([i for i in range(n)]):
            queens = set()
            for row, col in enumerate(perm):
                queens.add((row, col))
            ok = True
            for row, col in queens:
                others = queens - {(row, col)}
                for i in range(n):
                    if (i, col) in others or (row, i) in others:
                        ok = False
                        break
                if not ok:
                    break
                for delta_r, delta_c in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
                    r, c = row, col
                    while 0 <= r < n and 0 <= c < n:
                        if (r, c) in others:
                            ok = False
                            break
                        r += delta_r
                        c += delta_c
                    if not ok:
                        break
            if ok:
                grid = [['.'] * n for _ in range(n)]
                for r, c in queens:
                    grid[r][c] = 'Q'
                result.append([''.join(r) for r in grid])
        return result

from collections import defaultdict
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        if n_rows % 2:
            r_bound = n_rows // 2 + 1
        else:
            r_bound = n_rows // 2
        if n_cols % 2:
            c_bound = n_cols // 2 + 1
        else:
            c_bound = n_cols // 2

        n_op = 0
        n_one = 0
        freq = defaultdict(int)

        # print('bound', r_bound, c_bound)
        for r in range(r_bound):
            for c in range(c_bound):

                if r < r_bound - 1 or n_rows % 2 == 0:
                    if c < c_bound - 1 or n_cols % 2 == 0:
                        count = grid[r][c] + grid[r][n_cols-1-c] + grid[n_rows -1 - r][c] + grid[n_rows-1-r][n_cols-1-c]
                        # print(r, c)
                        if count <= 2:
                            n_op += count
                            n_one += count
                        else:
                            n_op += 4-count
                            n_one += 4-count
                    else:
                        # print('hi')
                        count = grid[r][c] + grid[n_rows-1-r][c]
                        freq[count] += 1
                else:
                    if c < c_bound - 1 or n_cols % 2 == 0:
                        # print(r, c)
                        count = grid[r][c] + grid[r][n_cols-1-c]
                        freq[count] += 1
                    else:
                        n_op += grid[r][c]

        # print(n_op, n_one, dict(freq))
        n_one += freq[2] // 2 * 2
        freq[2] -= freq[2] // 2 * 2
        if freq[2]:
            if freq[1] >= 2:
                return n_op + freq[1]
            else:
                if freq[2]:
                    if freq[1]:
                        return n_op + freq[1]
                    return n_op + 2
                else:
                    return n_op + freq[1]
        return n_op + freq[1]
                

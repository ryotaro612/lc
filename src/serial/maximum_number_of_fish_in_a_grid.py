from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    temp = grid[r][c]
                    grid[r][c] = 0
                    que = deque([(r, c)])
                    while que:
                        i, j = que.popleft()

                        for n_r, n_c in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c]:
                                temp += grid[n_r][n_c]
                                grid[n_r][n_c] = 0
                                que.append([n_r, n_c])
                    result = max(result, temp)
        
        return result


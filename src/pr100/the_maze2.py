from collections import deque

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n_row, n_col = len(maze), len(maze[0])
        d = [[float('inf')] * n_col for _ in range(n_row)]
        d[start[0]][start[1]] = 0
        que = deque([start])

        while que:
            r, c = que.popleft()

            for d_r, d_c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                row, col = r, c
                while  0 <= row + d_r < n_row and 0 <= col + d_c < n_col and maze[row+d_r][col+d_c] == 0:
                    row += d_r
                    col += d_c
                dist = abs(row - r) + abs(col - c) + d[r][c]   
                if dist < d[row][col]:
                    d[row][col] = dist
                    que.append([row, col])

        result = d[destination[0]][destination[1]]
        if result == float('inf'):
            return -1
        return result

from collections import deque, defaultdict


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        n_row, n_col = len(maze), len(maze[0])
        d = defaultdict(lambda: float("inf"))
        d[tuple(start)] = 0
        que = deque([start])

        while que:
            r, c = que.popleft()

            for d_r, d_c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                cur_r, cur_c = r, c
                while (
                    0 <= cur_r + d_r < n_row
                    and 0 <= cur_c + d_c < n_col
                    and maze[cur_r + d_r][cur_c + d_c] == 0
                ):
                    cur_r += d_r
                    cur_c += d_c

                if d[(cur_r, cur_c)] > d[(r, c)] + 1:
                    d[(cur_r, cur_c)] = d[(r, c)] + 1
                    que.append([cur_r, cur_c])

        return d[tuple(destination)] < float("inf")

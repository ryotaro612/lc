from collections import deque, defaultdict
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n_rows = len(grid)
        n_cols = len(grid[0])
        que = deque()
        
        cell_dict = defaultdict(lambda: -float('inf'))
        cell_dict[(0, 0)] = health - grid[0][0]
        que.append([0, 0, health - grid[0][0]])

        while que:
            r, c, h = que.popleft()
            if cell_dict[(r, c)] < h:
                continue
            
            for s_r, s_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                if 0 <= s_r < n_rows and 0 <= s_c < n_cols:
                    update_health = h - grid[s_r][s_c]
                    if cell_dict[(s_r, s_c)] < update_health:
                        cell_dict[(s_r, s_c)] = update_health
                        if cell_dict[(s_r, s_c)] >= 1:
                            que.append([s_r, s_c, update_health])
        
        return cell_dict[(n_rows-1, n_cols-1)] >= 1

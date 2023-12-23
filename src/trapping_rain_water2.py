from collections import deque

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n_rows = len(heightMap)
        n_cols = len(heightMap[0])
        max_height = max([v for row in heightMap for v in row])

        waters = [[max_height] * n_cols for _ in range(n_rows)]
        que = deque()
        for i in range(n_cols):
            que.append([0, i])
            que.append([n_rows-1, i])
        for i in range(n_rows):
            que.append([i, 0])
            que.append([i, n_cols-1])
        
        while que:
            r, c = que.popleft()
            if not ((0<=r<n_rows) and (0<= c < n_cols)):
                continue
            
            if r in {0, n_rows-1} or c in {0, n_cols - 1}:
                change = waters[r][c] != heightMap[r][c]
                waters[r][c] = heightMap[r][c]
            else:
                mini_height = min([waters[r-1][c], waters[r][c+1], waters[r+1][c], waters[r][c-1]])
                mini_height = max(heightMap[r][c], mini_height)
                change = mini_height != waters[r][c]
                waters[r][c] = mini_height
            
            if change:
                for n_r, n_c in [[r-1, c], [r,c+1], [r+1, c], [r, c-1]]:
                    que.append([n_r, n_c])
        
        result = sum([v for row in waters for v in row]) - sum([v for row in heightMap for v in row])
        return result 
            

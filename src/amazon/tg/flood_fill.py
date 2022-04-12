class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        que = deque()
        que.append((sr, sc))
        m = len(image) # n_row
        n = len(image[0]) # n_col
        color = image[sr][sc]
        done = [[False for _ in range(n)] for _ in range(m)]
        while 0 < len(que):
            r, c = que.popleft()
            if not(0 <= r and r < m and 0 <= c and c < n):
                continue
            if done[r][c]:
                continue
            if image[r][c] == color:
                image[r][c] = newColor
                done[r][c] = True
                for item in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                    que.append(item)
            
        return image

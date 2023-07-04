from collections import deque, defaultdict
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        d = defaultdict(lambda: float('inf'))
        d[(0, 0)] = 0
        que = deque([[0, 0]])

        while True:
            r, c = que.popleft()
            if [r, c] == [x, y]:
                return d[(r, c)]
            
            neighbors = []
            for ne_r in [r-2, r+2]:
                for ne_c in [c-1, c+1]:
                    neighbors.append([ne_r, ne_c])
            
            for ne_c in [c-2, c+2]:
                for ne_r in [r-1, r+1]:
                    neighbors.append([ne_r, ne_c])
            dist = d[(r, c)] + 1
            for [ne_r, ne_c] in neighbors:
                if dist < d[(ne_r, ne_c)]:
                    d[(ne_r, ne_c)] = dist
                    que.append([ne_r, ne_c])
        

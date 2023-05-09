from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        que = deque()

        n = len(board)
        d = [float('inf')] * (n*n)
        d[0] = 0
        que.append(0)

        while que:
            node = que.popleft()
            
            for i in range(node+1, min(node+7, n*n)):
                r, c = self.get_pos(i, n)
                print(i, r, c)
                if board[r][c] != -1:
                    i = board[r][c] - 1
                
                if d[i] > d[node] + 1:
                    d[i] = d[node] + 1
                    que.append(i)
        
        # print([(i, e) for i, e in enumerate(d)])
        if d[n*n-1] < float('inf'):
            return d[n*n-1]
        else:
            return -1
    def get_pos(self, node, n):
        r = n - 1 - node // n    
        c = node % n
        if node // n % 2:
            c = n - 1 - c
        return [r, c]

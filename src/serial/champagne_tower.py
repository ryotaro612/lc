from collections import deque

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        amount = [[0]*100 for _ in range(100)]
        que = deque()

        que.append([0,0])
        amount[0][0] = poured
        while que:
            r,c = que.popleft()
            if r == 99:
                amount[r][c] = max(1, amount[r][c])
                continue
            if amount[r][c] > 1:
                rest = amount[r][c] - 1
                amount[r][c] = 1
                amount[r+1][c] += rest / 2
                amount[r+1][c+1] += rest / 2
                que.append([r+1, c])
                que.append([r+1, c+1])

        return amount[query_row][query_glass]

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for f, t, w in edges:
            d[f][t] = w
            d[t][f] = w
        

        for k in range(n):
            for f in range(n):
                for t in range(n):
                    d[f][t] = min(d[f][t], d[f][k] + d[k][t])

        counter = []
        for i in range(n):
            counter.append(len([d[i][j] for j in range(n) if d[i][j] <= distanceThreshold]))
        
        a = min(counter)
        res = -1
        for i in range(n):
            if counter[i] == a:
                res = i
        return res

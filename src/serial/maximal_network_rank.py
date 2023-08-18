class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for node1, node2 in roads:
            g[node1].append(node2)
            g[node2].append(node1)

        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                temp = len(g[i]) + len(g[j])
                if j in g[i]:
                    temp -= 1
                result = max(result, temp)
        return result

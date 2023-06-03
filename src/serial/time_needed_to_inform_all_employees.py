class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for i, boss in enumerate(manager):
            if boss != -1:
                g[boss].append(i)

        return self.compute_time(g, headID, informTime)

    def compute_time(self, g, node, inform_time):
        result = 0

        for child in g[node]:
            result = max(
                result, inform_time[node] + self.compute_time(g, child, inform_time)
            )
        return result

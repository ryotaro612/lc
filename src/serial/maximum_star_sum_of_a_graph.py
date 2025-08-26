class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        """
        g[i] 0<=i<n
        val
        g[i].sort(reverse=True)
        result = 0
        """
        n = len(vals)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(vals[b])
            g[b].append(vals[a])
        
        result = max(vals)
        for i in range(n):
            cand = []
            for v in sorted(g[i], reverse=True):
                if v > 0 and len(cand) < k:
                    cand.append(v)
                else:
                    break
            result = max(result, sum(cand) + vals[i])

        return result

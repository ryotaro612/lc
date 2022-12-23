class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        n_path = len(targetPath)
        dp = [[float('inf')] * n for _ in range(n_path)]

        for i in range(n):
            target = targetPath[0]
            if names[i] == target:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        
        g = [[] for _ in range(n)]
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        
        for i, target in enumerate(targetPath):
            if i == 0:
                continue

            for node in range(n):
                base = float('inf')
                for neighbor in g[node]:
                    base = min(base, dp[i-1][neighbor])
                
                dp[i][node] = base
                if target != names[node]:
                    dp[i][node] += 1
            
        best = min(dp[n_path - 1])
        for node in range(n):
            if best == dp[n_path - 1][node]:
                start = node
                break
        
        result = [start]
        for i in range(n_path-2, -1, -1):
            best = float('inf')
            for node in g[result[-1]]:
                best = min(best, dp[i][node])
            for node in g[result[-1]]:
                if dp[i][node] == best:
                    result.append(node)
                    break
        return result[::-1]

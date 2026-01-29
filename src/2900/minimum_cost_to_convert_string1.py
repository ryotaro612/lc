import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        letters = [chr(ord('a') + i) for i in range(26)]
        g = {letter: {l: float('inf') if letter != l else 0 for l in letters} for letter in letters}
        
        for i in range(len(original)):
            g[original[i]][changed[i]] = min(g[original[i]][changed[i]], cost[i])

        for a in letters:
            for b in letters:
                for c in letters:
                    g[b][c] = min(g[b][c], g[b][a] + g[a][c])
        
        result = 0
        for a, b in zip(source, target):
            result += g[a][b]
        
        if result == float('inf'):
            return -1
        return result

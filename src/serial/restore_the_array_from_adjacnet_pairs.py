from collections import deque, defaultdict, Counter
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        counter = Counter([v for item in adjacentPairs for v in item])
        min_freq = float('inf')
        for d, f in counter.items():
            if f < min_freq:
                min_freq = f
                result = [d]
                
        pair_map = defaultdict(lambda: defaultdict(int))
        for a, b in adjacentPairs:
            pair_map[a][b] += 1
            pair_map[b][a] += 1
        
        
        while len(result) <= len(adjacentPairs):
            k = next(iter(pair_map[result[-1]]))
            pair_map[result[-1]][k] -= 1
            pair_map[k][result[-1]] -= 1
            if not pair_map[result[-1]][k]:
                del pair_map[result[-1]][k]
                del pair_map[k][result[-1]]
            
            result.append(k)
            
        return result

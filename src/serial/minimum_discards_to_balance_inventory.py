from collections import deque, defaultdict

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        result = 0
        freq = defaultdict(deque)
        
        for i, num in enumerate(arrivals):
            if len(freq[num]) + 1 > m:
                result += 1
            else:
                freq[num].append(i)
            if i + 1 - w >= 0:
                if freq[arrivals[i+1-w]]:
                    if freq[arrivals[i+1-w]][0] == i + 1 - w:
                        freq[arrivals[i+1-w]].popleft()
        return result   

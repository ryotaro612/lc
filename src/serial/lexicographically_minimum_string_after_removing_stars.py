import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        """
        a*aba
        """
        n = len(s)
        keep = [True] * n
        heap = []
        for i, c in enumerate(s):
            if c == '*':
                keep[i] = False
                _, j = heapq.heappop(heap)
                keep[-j] = False
                continue
            heapq.heappush(heap, (c, -i))
        
        
        return ''.join([s[i] for i in range(n) if keep[i]])


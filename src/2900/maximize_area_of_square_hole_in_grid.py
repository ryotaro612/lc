class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        """
        hBars
        [i, i+1, i+2,...i+j] -> j+1
        vBars
        k + 1
        edge = min((j+2), (k+2))
        edge**2
        """
        h = self.measure(sorted(hBars))
        v = self.measure(sorted(vBars))

        return min(h+1, v+1)**2
    
    def measure(self, bars):
        for i, bar in enumerate(bars):
            if i == 0:
                current = 1
                result = 1
            else:
                if bars[i] -1 == bars[i-1]:
                    current += 1
                    result = max(result, current)
                else:
                    current = 1
        return result

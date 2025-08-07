class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """
        ax + by = c
        a + 7b = c
        5a + 3b = c
        
        (y2-y1) /(x2-x1) == 
        """
        stockPrices.sort()
        s = stockPrices
        n = len(s)
        if n <= 1:
            return 0
        result = 1
        
        for i in range(n-2):
            if (s[i+1][1] - s[i][1]) * (s[i+2][0] - s[i+1][0])  != (s[i+2][1] - s[i+1][1]) * (s[i+1][0] - s[i][0]) :
                result += 1
        
        return result

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        
        for i in range(1, 10):
            self.find(high, i, result)
            
        return sorted([v for v in result if low <= v])

    def find(self, high, val, result):
        if val <= high:
            result.append(val)
        if val % 10 < 9:
            self.find(high, val*10+(val%10+1), result)

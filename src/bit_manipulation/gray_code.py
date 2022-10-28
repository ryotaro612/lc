class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        base = self.grayCode(n-1)
        
        return base + [(1 << (n-1)) | v for v in reversed(base)]

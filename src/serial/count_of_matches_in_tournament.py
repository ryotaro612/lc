class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            if n % 2:
                result += (n-1) // 2
                n = (n-1) // 2 + 1
            else:
                n //= 2
                result += n
        return result
            

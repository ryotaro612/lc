class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        result = 0
        while True:
            digits = [ord(c) - ord('0') for c in str(n)]
            
            if sum(digits) <= target:
                return result
            
            for rightmost in range(len(digits)):
                if digits[len(digits) - 1 - rightmost]:
                    break
            
            add = (10 - digits[len(digits) - 1 - rightmost]) * (10**rightmost)
            result += add
            n += add

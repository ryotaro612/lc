class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev, prev2, current = 1, 0, 0
        
        for i in range(1, n+1):
            current = prev + prev2
            prev2 = prev
            prev = current
        return current

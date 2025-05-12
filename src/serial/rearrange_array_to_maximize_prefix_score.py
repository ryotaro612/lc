class Solution:
    def maxScore(self, nums: List[int]) -> int:
        arranged = [e for e in nums if e > 0] + sorted([e for e in nums if e <= 0], reverse= True)
        result = 0
        prefix = 0
        for e in arranged:
            prefix += e
            if prefix > 0:
                result += 1
        
        return result

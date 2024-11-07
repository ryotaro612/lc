class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0
        for i in range(32):
            counter = 0
            for candidate in candidates:
                if (candidate >> i) & 1:
                    counter += 1
        
            result = max(result, counter)
        
        return result

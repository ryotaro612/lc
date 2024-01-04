from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        n
        (n - n // 3 * 3)
        n // 3 + (n-n//3 * 3) // 2
        n // 3 - 1
        """
        counter = Counter(nums)
        result = 0
        for freq in counter.values():
            if freq == 1:
                return -1
            
            num_3 = freq // 3
            for cand in range(num_3, -1, -1):
                if (freq - cand * 3) % 2 == 0:
                    result += cand + (freq - cand * 3) // 2
                    break
        return result 

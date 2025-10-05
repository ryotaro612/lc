
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        n_digit = len(str(nums[0]))

        for i in range(n_digit):
            freq = [0] * 10
            for j in range(n):
                freq[ord(str(nums[j])[i]) - ord('0')] += 1
            
            total = sum(freq)
            for k in range(10):
                
                result += freq[k] * (total - freq[k])
        
        return result // 2

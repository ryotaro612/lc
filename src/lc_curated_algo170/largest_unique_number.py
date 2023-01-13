class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        onces = [k for k, freq in Counter(nums).items() if freq == 1]
        if onces:
            return max(onces)
        else:
            return -1
        

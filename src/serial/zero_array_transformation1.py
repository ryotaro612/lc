class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """
        [i, j]
        prefix[i] += -1
        prefix[j+1] += 1
        prefix[k] += prefix[k-1]
        """
        n = len(nums)
        prefix = [0] * (n+1)

        for start, end in queries:
            prefix[start] -= 1
            prefix[end+1] += 1
        
        for i in range(n):
            prefix[i+1] += prefix[i]
        
        for i in range(n):
            if nums[i] + prefix[i] > 0:
                return False
        
        return True

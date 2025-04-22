class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        """
        """
        result = 0
        n = len(nums)
        m = len(pattern)
        for i in range(n-m):
            
            for k in range(m):
                if pattern[k] == 1:
                    if not nums[i+k+1] > nums[i+k]:
                        break
                elif pattern[k] == 0:
                    if nums[i+k+1] != nums[i+k]:
                        break
                else:
                    if not nums[i+k+1] < nums[i+k]:
                        break
            else:
                result += 1
        
        return result

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        """
        """
        result = 0
        n = len(nums)
        m = len(pattern)
        for i in range(n):
            sub = nums[i:i+m+1]
            if len(sub) < m + 1:
                break
            
            for i in range(m):
                if pattern[i] == 1:
                    if not sub[i+1] > sub[i]:
                        break
                elif pattern[i] == 0:
                    if sub[i+1] != sub[i]:
                        break
                else:
                    if not sub[i+1] < sub[i]:
                        break
            else:
                result += 1
        
        return result

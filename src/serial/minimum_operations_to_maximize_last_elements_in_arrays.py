import math
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        result = self.count(nums1, nums2)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1] 

        result = min(result, 1 + self.count(nums1, nums2))
        return result if math.inf > result else -1

    def count(self, nums1, nums2):
        n = len(nums1)
        ops = 0
        for i in range(n-1):
            if nums1[i] <= nums1[n-1] and nums2[i] <= nums2[n-1]:
                continue
            if nums2[i] <= nums1[n-1] and nums1[i] <= nums2[n-1]:
                ops += 1
            else:
                ops = math.inf            
               
        return ops

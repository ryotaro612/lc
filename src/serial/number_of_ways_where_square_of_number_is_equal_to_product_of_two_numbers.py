from collections import defaultdict

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        nums1[i]**2
        """
        t1 = self.solve(nums1, nums2)
        t2 = self.solve(nums2, nums1)
        
        return t1 + t2
        
    def solve(self, nums1, nums2):
        freq = defaultdict(int)
        for num in nums1:
            freq[num**2] += 1

        result = 0
        n = len(nums2)
        for j in range(n):
            for k in range(j+1, n):
                result += freq[nums2[j] * nums2[k]]


        return result

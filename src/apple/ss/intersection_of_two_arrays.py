class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1, n2 = len(nums1), len(nums2)
        i1, i2 = 0, 0
        result = []
        
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                if len(result) == 0 or result[-1] != nums1[i1]:
                    result.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return result

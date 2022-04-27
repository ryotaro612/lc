class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        nums2_iter = iter(nums2)
        i = 0 
        v2 = next(nums2_iter, None)
        while i < len(nums1) and v2 is not None:        
            if nums1[i] == v2:
                result.append(v2)
                i += 1
                v2 = next(nums2_iter, None)
            elif nums1[i] < v2:
                i += 1
            else:
                v2 = next(nums2_iter, None)
                
        return result
            

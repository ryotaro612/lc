from collections import Counter
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)

        uniq1 = {num for num in nums1 if num not in set2}
        uniq2 = {num for num in nums2 if num not in set1}

        result = 0
        n = len(nums1)
        n1 = min(n//2, len(uniq1))
        n2 = min(n//2, len(uniq2))
        result = n1 + n2

        inter = set1 & set2

        return result + min(len(inter), n//2 - n1 + n//2 - n2)

from collections import defaultdict
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2
        val_idx = defaultdict(list)
        for i, v in enumerate(nums2):
            val_idx[v].append(i)
        result = []

        for v in nums1:
            result.append(val_idx[v].pop())

        return result

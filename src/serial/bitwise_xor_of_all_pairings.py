class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        for v in nums1:
            xor1 ^= v
        xor2 = 0
        for v in nums2:
            xor2 ^= v
        
        if len(nums1) % 2:
            if len(nums2) % 2:
                return xor1 ^ xor2
            else:
                return xor2
        else:
            if len(nums2) % 2:
                return xor1
            else:
                return 0

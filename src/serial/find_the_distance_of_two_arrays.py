class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        answer = [
            list({v for v in nums1 if v not in s2}),
            list({v for v in nums2 if v not in s1}),
        ]
        return answer

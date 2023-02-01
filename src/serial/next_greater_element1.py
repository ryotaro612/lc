class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        v_to_i = {v: i for i, v in enumerate(nums2)}
        result = []
        for num in nums1:
            i = v_to_i[num]
            for j in range(i+1, len(nums2)):
                if num < nums2[j]:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result

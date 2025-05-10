class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        n_zero > 0
        >= sum(num1) + n_zero
        """
        n_zero1 = len([e for e in nums1 if e == 0])
        n_zero2 = len([e for e in nums2 if e == 0])
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if n_zero1 == 0:
            if n_zero2 == 0:
                if sum1 == sum2:
                    return sum1
                else:
                    return -1
            else:
                if sum2 + n_zero2 <= sum1:
                    return sum1
                else:
                    return -1
        else:
            if n_zero2 == 0:
                if sum1 + n_zero1 <= sum2:
                    return sum2
                else:
                    return -1
            else:
                return max(sum1 + n_zero1, sum2 + n_zero2)
        

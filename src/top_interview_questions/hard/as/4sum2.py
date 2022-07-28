"""
table[nums1[i]+num2[j]] = num_of(i, j)


"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) ->   int:
        n = len(nums1)
        nums_sum_freq = dict()
        for i in range(n):
            for j in range(n):
                added = nums1[i] + nums2[j]
                nums_sum_freq.setdefault(added, 0)
                nums_sum_freq[added] += 1
        result = 0
        for i in range(n):
            for j in range(n):
                
                result += nums_sum_freq.get(-(nums3[i] + nums4[j]), 0)
                
        return result

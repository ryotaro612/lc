from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        count_ary[n+1]
        count_ary[i] = [0..i)
        i..n-1 count_ary[n] - count_ary[i]
        """
        counter = Counter(nums)
        dom_val = None
        dom_freq = None
        for k, v in counter.items():
            if dom_val is None:
                dom_val = k
                dom_freq = v
            elif dom_freq < v:
                dom_freq = v
                dom_val = k

        n = len(nums)
        freq_ary = [0] * (n+1)
        for i in range(n):
            freq_ary[i+1] += freq_ary[i]
            if nums[i] == dom_val:
                freq_ary[i+1] += 1

        for i in range(n-1):
            if freq_ary[i+1] > (i + 1- freq_ary[i+1]):

                right_dom = freq_ary[n] - freq_ary[i+1]
                rest = n - i - 1
                if right_dom > rest - right_dom:
                    return i
        return -1 
            

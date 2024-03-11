class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        d[diff]
        n(0) - n(1)
        d[1] = 0
        d[0] = 1
        d[n(0) - n(1)] = max index

        freq_0 = 0
        freq_1 = i + 1 - freq_0
        result = 0
        d[freq_1 - freq_0] - i + 1
        """
        diff_index = dict()
        n = len(nums)
        freq_1 = 0
        for i, num in enumerate(nums):
            if num:
                freq_1 += 1
            freq_0 = i + 1 - freq_1
            #print(i, freq_0, freq_1)
            diff_index[freq_0 - freq_1] = i
        # print(diff_index)
        freq_0, freq_1 = 0, 0
        result = 0
        for i, num in enumerate(nums):
            if freq_0 - freq_1 in diff_index:
                result = max(result, diff_index[freq_0-freq_1] - i + 1)
            if num:
                freq_1 += 1
            freq_0 = i + 1 - freq_1
        return result 

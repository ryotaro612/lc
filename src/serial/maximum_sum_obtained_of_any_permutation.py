class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        requests[i] =s1, e1
        freq[s1] += 1
        freq[e1+1] -= 1
        """
        n = len(nums)
        freq = [0] * (n+1)
        for start, end in requests:
            freq[start] += 1
            freq[end+1] -= 1
        
        for i in range(n):
            freq[i+1] += freq[i]
        freq = freq[:n]
        freq_i = sorted([[f, i] for i, f in enumerate(freq)])
        ordered_nums = sorted(nums)
        new_nums = [0] * n
        for i in range(n):
            new_nums[freq_i[i][1]] = ordered_nums[i]
        
        result = 0
        for i in range(n):
            result += new_nums[i] * freq[i]
            result %= (10**9+7)
        return result

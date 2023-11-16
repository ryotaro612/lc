class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        for i in range(1<<n):
            pattern = ['0'] * n
            for j in range(n):
                if i & (1<<j):
                    pattern[j] = '1'
            cand = ''.join(pattern)
            if cand not in nums_set:
                return cand

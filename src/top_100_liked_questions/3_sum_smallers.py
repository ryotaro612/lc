from collections import defaultdict

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(3)]
        n = len(nums)
        for num in nums:
            temp = [defaultdict(int) for _ in range(2)]
            for i in range(2):
                for k, freq in dp[i].items():
                    temp[i][k+num] += freq
            
            dp[0][num] += 1
            for i in range(2):
                for k, freq in temp[i].items():
                    dp[i+1][k] += freq
        result = 0
        for k, v in dp[2].items():
            if k < target:
                result += v
        return result

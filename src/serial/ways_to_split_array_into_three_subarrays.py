class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        
        j = 2
        k = j
        result = 0
        mod = 10**9+7
        # 0 1 2
        for i in range(1, n-1):
            j = max(i+1, j)
            while j < n-1 and prefix[i] > prefix[j] - prefix[i]:
                j += 1
            
            k = max(j, k)
            while k < n - 1 and prefix[n] - prefix[k+1] >= prefix[k+1] - prefix[i]:
                k += 1
            
            # print(i, j, k)
            if prefix[i] <= prefix[k] - prefix[i] <= prefix[n] - prefix[k]:
                result += k - j + 1
                result %= mod
        
        return result

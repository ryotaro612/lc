class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        n = len(nums)
        dp[0<=i<=n-1][0-1] dp[i][0] longest 0 ==
        dp[i][1] 1

        even =
        odd = 

        i 
        """
        n = len(nums)
        dp = [[1] * 2 for _ in range(n)]
        
        even = [i for i, num in enumerate(nums) if num % 2 == 0][::-1]
        odd = [i for i, num in enumerate(nums) if num % 2][::-1]
        
        for i in range(n):
            if nums[i] % 2:
                dp[i][1] = 1
            else:
                dp[i][0] = 1


        for i in range(n):
            while even and even[-1] <= i:
                even.pop()
            while odd and odd[-1] <= i:
                odd.pop()
            
            if nums[i] % 2:
                if even:
                    dp[even[-1]][1] = max(dp[even[-1]][1], dp[i][1] + 1)
                if odd:
                    dp[odd[-1]][0] = max(dp[odd[-1]][0], dp[i][0] + 1)
            else: # even
                if even:
                    dp[even[-1]][0] = max(dp[even[-1]][0], dp[i][0] + 1)
                if odd:
                    dp[odd[-1]][1] = max(dp[odd[-1]][1], dp[i][1] + 1)
        
        return max([v for arr in dp for v in arr])
        

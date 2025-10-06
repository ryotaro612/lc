class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        dp = [0] * 2
        dp[0]
        dp[i][0] ary[i] < arr[i+1] dp[i+1][0]= dp[i][0] + 1 else 0
        dp[i][1]        >
        """
        n = len(arr)
        dp = [1] * 2
        result = 1
        for i in range(1, n):
            temp = [0] * 2
            if i % 2:
                if arr[i-1] < arr[i]:
                    temp[0] = dp[0] + 1
                    temp[1] = 1
                elif arr[i-1] > arr[i]:
                    temp[1] = dp[1] + 1
                    temp[0] = 1
                else:
                    temp[0] = temp[1] = 1
            else:
                if arr[i-1] > arr[i]:
                    temp[0] = dp[0] + 1
                    temp[1] = 1
                elif arr[i-1] < arr[i]:
                    temp[1] = dp[1] + 1
                    temp[0] = 1
                else:
                    temp[0] = temp[1] = 1
            dp = temp
            # print(i, temp)
            result =max(result, max(dp))
        
        return result
                

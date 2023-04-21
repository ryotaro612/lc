"""
100
100
[2,5,36,2,5,5,14,1,12,1,14,15,1,1,27,13,6,59,6,1,7,1,2,7,6,1,6,1,3,1,2,11,3,39,21,20,1,27,26,22,11,17,3,2,4,5,6,18,4,14,1,1,1,3,12,9,7,3,16,5,1,19,4,8,6,3,2,7,3,5,12,6,15,2,11,12,12,21,5,1,13,2,29,38,10,17,1,14,1,62,7,1,14,6,4,16,6,4,32,48]
[21,4,9,12,5,8,8,5,14,18,43,24,3,0,20,9,0,24,4,0,0,7,3,13,6,5,19,6,3,14,9,5,5,6,4,7,20,2,13,0,1,19,4,0,11,9,6,15,15,7,1,25,17,4,4,3,43,46,82,15,12,4,1,8,24,3,15,3,6,3,0,8,10,8,10,1,21,13,10,28,11,27,17,1,13,10,11,4,36,26,4,2,2,2,10,0,11,5,22,6]

"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        n_group = len(group)
        dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(n_group+1)]
        mod = 10**9 + 7
        dp[0][0][0] = 1
        for g in range(n_group):
            for i in range(n+1):
                for p in range(minProfit+1):
                    if i + group[g] <= n:
                        new_num = i + group[g]
                        new_profit = min(minProfit, p+profit[g])
                        dp[g+1][new_num][new_profit] += dp[g][i][p]
                        dp[g+1][new_num][new_profit] %= mod

                    dp[g+1][i][p] += dp[g][i][p]
                    dp[g+1][i][p] %= mod
        
        result = 0
        for i in range(n+1):
            result += dp[n_group][i][minProfit]
            result %= mod
        return result

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profits = [0] * (n+1)
        sell = [0] * (n+1)
        for i in range(n):
            profits[i+1] = profits[i] + prices[i] * strategy[i]
            sell[i+1] = sell[i] + prices[i]

        result = profits[n]
    
        for i in range(n-k+1):
            cand = profits[i]
            cand += sell[i+k] - sell[i+(k//2)]
            cand += profits[n] - profits[i+k]
            result = max(result, cand)
        
        return result
        

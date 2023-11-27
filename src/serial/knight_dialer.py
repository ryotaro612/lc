class Solution:
    def knightDialer(self, n: int) -> int:
        prev = [1] * 10
        mod = 10**9 + 7
        movable = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        for _ in range(1, n):
            dp = [0] * 10
            for i in range(10):
                for next_i in movable[i]:
                    dp[next_i] += prev[i]
                    dp[next_i] %= mod
            prev = dp
        
        result = 0
        for v in prev:
            result += v
            result %= mod
        return result
        

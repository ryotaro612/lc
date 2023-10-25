import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [float('inf')] * n
        dp[0] = 1
        pointers = [0] * len(primes)
        for i in range(0, n-1):
            for j, prime in enumerate(primes):
                dp[i+1] = min(dp[i+1], dp[pointers[j]] * prime)
            for j, prime in enumerate(primes):
                if dp[i+1] == dp[pointers[j]] * prime:
                    pointers[j] += 1
        # print(dp)
        return dp[n-1]

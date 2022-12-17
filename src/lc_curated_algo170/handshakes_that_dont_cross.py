class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        memo = dict()
        return self.rec(numPeople, memo)
    
    def rec(self, n, memo):
        if n in memo:
            return memo[n]
        if n in {2, 0}:
            memo[n] = 1
            return memo[n]
        result = 0
        mod = 1000000000 + 7
        for i in range(1, n, 2):
            a = self.rec(i-1, memo)
            b = self.rec(n - i-1, memo)
            result += (a * b) % mod
            result %= mod
        memo[n] = result
        return memo[n]

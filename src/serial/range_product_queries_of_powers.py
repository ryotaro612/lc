class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        n
        15
        """
        powers = []
        for i in range(31):
            if n & (1<<i):
                powers.append(1<<i)
        
        result = []
        mod = 10**9 + 7
        for left, right in queries:
            res = 1
            for i in range(left, right+1):
                res *= powers[i]
                res %= mod

            result.append(res)
        
        return result

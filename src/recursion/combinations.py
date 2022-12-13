class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        memo = dict()
        
        result= self.rec(1, memo, n, k)
        # print(memo)
        return result
        
    def rec(self, v, memo, n, k):
        key = (v, k)
        if (v, k) in memo:
            return memo[key]
        if v > n:
            memo[key] = []
            return memo[key]
        
        result = []
        if k == 1:
            result.append([v])
        
        result.extend(self.rec(v+1, memo, n, k))
        for item in self.rec(v+1, memo, n, k - 1):
            result.append([v] + item)
        memo[key] = result
        return memo[key]
    

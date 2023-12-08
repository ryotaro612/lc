class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cache = dict()

        return self.rec(1, n+1, cache)
    
    def rec(self, left, right, cache):
        if (left, right) in cache:
            return cache[(left, right)]
        if right <= left:
            return 0
        if left + 1 == right:
            cache[(left, right)] = 0
            return 0
        res = float('inf')
        for selection in range(left, right):
            res = min(res, selection + max(self.rec(left, selection, cache), self.rec(selection+1, right, cache)))
        cache[(left, right)] = res
        return res

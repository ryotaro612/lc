from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        AAB
        freq = [2, 1]
        [1, 1]
        """
        counter = Counter(tiles)
        return self.rec(list(counter.values()), []) - 1

    def rec(self, vals, temp):
        if len(temp) == len(vals):
            total = self.fact(sum(temp))
            for a in [self.fact(v) for v in temp]:
                total //= a
            return total
        
        res = 0
        for i in range(vals[len(temp)]+1):
            temp.append(i)
            res += self.rec(vals, temp)
            temp.pop()
        
        return res
    

    def fact(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res

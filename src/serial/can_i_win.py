from functools import cache

class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        return self.rec((1<<maxChoosableInteger) - 1, maxChoosableInteger, desiredTotal)
    @cache    
    def rec(self, options, maxChoosableInteger, desiredTotal):
        # print(options, desiredTotal)
        if desiredTotal <= 0:
            return True
        result = True
        for i in range(maxChoosableInteger):
            if (1 << i) & options:
                if desiredTotal <= i + 1:
                    return True
                else:
                    mask = ~(1<<i) & options
                    if not self.rec(mask, maxChoosableInteger, desiredTotal - (i+1)):
                        return True
            i += 1
        # print(options)
        return False

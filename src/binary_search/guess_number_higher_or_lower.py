# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        lb = 0
        ub = 2**31
        while ub - lb > 0:
            mid = (ub + lb) // 2
            v = guess(mid)
            
            if v == -1:
                ub = mid
            elif v== 1:
                lb = mid
            else:
                return mid
        

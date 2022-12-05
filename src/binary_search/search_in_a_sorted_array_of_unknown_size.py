# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        ub = 10001
        lb = -1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            result = reader.get(mid)
            if result == (1 << 31) - 1:
                ub = mid
            elif target < result:
                ub = mid
            else:
                lb = mid
        
        if reader.get(lb) == target:
            return lb
        else:
            return -1

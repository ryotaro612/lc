from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = defaultdict(list)
        n_row = len(nums)
        for r, row in enumerate(nums):
           for c, v in enumerate(row):
               diag[r+c].append(v)

        result = []
        keys = sorted(diag.keys())
        for key in keys:
            result.extend(diag[key][::-1])
        
        return result
        

"""
[0,0,0,0,0,0,0,0,0,0,0,0]
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n_one = sum(data)
        n = len(data)
        if n_one == 0:
            return 0
        n_zero = 0
        for i in range(n_one):
            if data[i] == 0:
                n_zero += 1
        result = n_zero
        if data[0] == 0:
            n_zero -= 1
        for left in range(1, n-(n_one-1)):
            if data[left+n_one-1] == 0:
                n_zero += 1
            result = min(result, n_zero)
            if data[left] == 0:
                n_zero -= 1
        
        return result

import itertools
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        result = 0
        for order in itertools.permutations(nums):
            i = 0
            cand = 0
            for e in order:
                n_bits = 0
                temp = e
                while temp:
                    n_bits += 1
                    temp >>= 1
                cand <<= n_bits

                cand += e
            
            result = max(result, cand)
        return result

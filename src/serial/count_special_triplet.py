from collections import defaultdict
import bisect

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        """
        num * 2, i

        v < i
        v2 > i
        v * v2
        """
        val_idx = defaultdict(list)

        for i, num in enumerate(nums):
            val_idx[num].append(i)
        
        result = 0
        mod = 10**9 + 7
    
        for j, num in enumerate(nums):
            found = bisect.bisect_left(val_idx[num*2], j)
            n = len(val_idx[num*2])

            left = found
            if found < n and val_idx[num*2][found] == j:
                right = n - (found+1)
            else:
                right = n - found
            
            result += left * right
            result %= mod
        
        return result

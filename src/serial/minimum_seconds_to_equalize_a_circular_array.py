from collections import defaultdict
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        """
        val -> index []

        2 -> [0, 4, 5, 9] # len(nums) = 11
        0 -> 4, 9  -> *4*

        2 -> [0] unique -> *n*

        (*4* + 1) // 2 <- 
        """
        result = float('inf')

        n = len(nums)
        val_idx = defaultdict(list)
        for i, num in enumerate(nums):
            val_idx[num].append(i)
        
        for idx in val_idx.values():
            dist = 0
            if len(idx) == 1:
                dist = n
            else:
                for i in range(len(idx)):
                    if i == 0:
                        # n = 4 [1, 3]
                        dist = max(dist, idx[1] - idx[0], n-idx[-1] + idx[0])
                    elif i == len(idx) - 1:
                        dist = max(dist, idx[-1] - idx[-2], n - idx[-1] + idx[0])
                    else:
                        dist = max(dist, idx[i+1] - idx[i], idx[i] - idx[i-1])
            
            # 0 -> 0, 1 -> 0, 2 -> 1, 3 -> 1, 4 -> 2
            result = min(result, dist // 2)
        
        return result




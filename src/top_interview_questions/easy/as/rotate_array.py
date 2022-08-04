"""
[1,2,3,4,5,6]
3

[1,2,3,4,5,6,2,38,1,-1]
3

[1,2,3,4,5,6,2,38,1,-1]
1
"""

import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return
        n_loop = math.lcm(n, k) // k

        count = 0
        for i in range(n):
            j = i
            temp = nums[j]
            for _ in range(n_loop):
                if count < n:
                    next_j = (j + k) % n
                    next_temp = nums[next_j]
                    nums[next_j] = temp
                    j = next_j
                    temp = next_temp
                    count += 1
                else:
                    return

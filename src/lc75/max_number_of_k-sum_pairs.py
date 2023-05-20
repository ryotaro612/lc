"""
[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
2
"""
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)

        result = 0
        for num in counter:
            if num == k - num:
                if counter[num] % 2:
                    result += counter[num] - 1
                else:
                    result += counter[num]
            else:
                result += min(counter[num], counter.get(k - num, 0))

        return result // 2

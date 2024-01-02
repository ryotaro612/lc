from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        n_rows = max([v for v in counter.values()])
        result = [[] for _ in range(n_rows)]

        nums.sort()
        pos = 0
        for v in nums:
            result[pos].append(v)
            pos = (pos + 1) % n_rows
        
        return result

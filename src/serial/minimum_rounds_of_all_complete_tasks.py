from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0
        for num in nums:
            neighbor = max(counter.get(num -1, 0), counter.get(num+1, 0))
            if neighbor:
                result = max(result, counter[num] + neighbor)
        return result 

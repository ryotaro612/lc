from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        result = [0, 0]
        for i in range(1, n+1):
            if counter[i] == 0:
                result[1] = i
            elif counter[i] == 2:
                result[0] = i
        return result
        

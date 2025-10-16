from collections import defaultdict
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num % value] += 1
        
        result = 0
        while True:
            if counter[result % value]:
                counter[result % value] -= 1

                result += 1
            else:
                return result

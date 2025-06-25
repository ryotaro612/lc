from collections import Counter
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        """
        7, 777
        77,77
        777,7
        """
        counter = Counter(nums)

        result = 0
        n = len(target)
        for i in range(1, n):
            if target[:i] == target[i:]:
                freq = counter.get(target[:i], 0)
                result += freq * (freq-1)
            else:
                result += counter.get(target[:i], 0) * counter.get(target[i:], 0)

        return result

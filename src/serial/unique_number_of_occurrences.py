from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        nums = set()
        for v in counter.values():
            if v in nums:
                return False
            nums.add(v)

        return True        

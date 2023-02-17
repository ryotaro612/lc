from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        result = 0
        for num in arr:
            if counter.get(num+1, 0):
                result += 1
        return result

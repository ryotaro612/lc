from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        result = 0
        for k, v in counter.items():
            while v > 0:
                result += k + 1
                v -= k + 1
        
        return result

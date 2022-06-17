import itertools
"""
1 -> 1
2 -> 4
3 -> 4 * 4 + 4 * 4 + 4 * 4
f(n) -> f(n-1) * f(n-1) * 8

[1,9,1,2]
(9-1) * (1+2)
"""
class Solution:
    
    def judgePoint24(self, cards: List[int]) -> bool:
        for pattern in itertools.permutations(cards):
            # print(pattern)
            for val in self.compute(pattern):
                if val[0] % val[1] == 0 and val[0] // val[1] == 24:
                    return True
        return False
    
    def compute(self, pattern):
        if len(pattern) == 1:
            return [(pattern[0], 1)]
        result = []
        for i in range(1, len(pattern)):
            left = self.compute(pattern[:i])
            right = self.compute(pattern[i:])
            result.extend(self.compute_combi(left, right))
        
        result = list(set(result))
        return result
    
    def compute_combi(self, lefts, rights):
        result = []
        for left in lefts:
            for right in rights:
                result.append((left[0] * right[1] + left[1] * right[0], left[1] * right[1]))
                result.append((left[0] * right[1] - left[1] * right[0], left[1] * right[1]))
                result.append((left[0] * right[0], left[1] * right[1])) 
                result.append((left[0] * right[1], left[1] * right[0])) 
        
        return [val for val in result if val[1] != 0]

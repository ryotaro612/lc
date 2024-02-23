class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * n
        trust_count = [0] * n
        for a, b in trust:
            count[b-1] += 1
            trust_count[a-1] += 1
        
        result = [i for i, a in enumerate(count) if a == n - 1 and trust_count[i]==0]
        
        if len(result) == 1:
            return result[0] + 1
        return -1

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = (n+m) * mean
        rest = total - sum(rolls)
        result = [0] * n
        for i in range(rest):
            result[i % n] += 1
        
        if all([0<v<=6 for v in result]):
            return result
        return []

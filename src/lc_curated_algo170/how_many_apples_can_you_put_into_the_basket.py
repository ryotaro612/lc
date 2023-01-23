class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight = sorted(weight)
        total = 0
        n = len(weight)
        for i in range(n):
            if total + weight[i] <= 5000:
                total += weight[i]
            else:
                return i
        return n

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        special.sort()

        result = special[0] - bottom
        n = len(special)
        for i in range(n-1):
            result = max(result, special[i+1] - special[i] - 1)
        
        result = max(result, top - special[-1])
        return result

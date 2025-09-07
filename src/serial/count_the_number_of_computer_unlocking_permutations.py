class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        """
        complexity[0]
        (n - 1)!
        """
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        
        mod = 10**9+7
        result = 1
        for i in range(1, n):
            result *= i
            result %= mod
        
        return result

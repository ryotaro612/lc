class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        """
        positive -> 
        """
        mod = 10**9 + 7
        if k == 1:
            return self.find(arr) % mod
        
        result = self.find(arr + arr)
        total = sum(arr)
        if total <= 0:
            return result % mod 

        return (result + total * (k-2)) % mod

    def find(self, arr):
        n = len(arr)
        right = [0] * n
        right[n-1] = max(0, arr[n-1])
        for i in range(n-2, -1, -1):
            right[i] = max(0, arr[i] + right[i+1])
        
        return max(right)

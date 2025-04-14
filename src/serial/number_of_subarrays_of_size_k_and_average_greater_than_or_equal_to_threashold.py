class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0
        result = 0
        total = sum(arr[:k])
        if total >= threshold * k:
            result += 1
        
        for i in range(k, n):
            total -= arr[i-k]
            total += arr[i]

            if total >= threshold * k:
                result += 1
        
        return result

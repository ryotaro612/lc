from collections import defaultdict
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        freq = [defaultdict(int) for _ in range(n)]
        for j in range(n):
            val = 0
            for l in range(j): 
                freq[j][prefix[j] ^ prefix[l]] += 1
    
        result = 0
        for k in range(1, n):
            for j in range(1, k+1):
                result += freq[j][prefix[k+1] ^ prefix[j]]
        return result

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        prefix[i] = arr[0] ^ arr[1] ^ ... arr[i-1]
        left, right
        prefix[right+1] ^ prefix[left]
        """
        n = len(arr)
        prefix = [0] *(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        result = []
        for left, right in queries:
            result.append(prefix[left] ^ prefix[right+1])
        
        return result

    

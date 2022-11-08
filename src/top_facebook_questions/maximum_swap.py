class Solution:
    def maximumSwap(self, num: int) -> int:
        result = num
        num_str = [c for c in str(num)]
        n = len(num_str)
        
        for i in range(n-1):
            for j in range(i+1, n):
                num_str[i], num_str[j] = num_str[j], num_str[i]
                result = max(result, int(''.join(num_str)))
                num_str[i], num_str[j] = num_str[j], num_str[i]
        return result
                

class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefix = []
        n = len(s)
        prefix_a = [0] * (n+1) 
        prefix_b = [0] * (n+1)
        for i, c in enumerate(s):
            prefix_a[i+1] = prefix_a[i]
            prefix_b[i+1] = prefix_b[i]
            if c == 'a':
                prefix_a[i+1] += 1
            else:
                prefix_b[i+1] += 1 

        result = float('inf')
        for i, c in enumerate(s):
            if c == 'a':
                result = min(result, prefix_b[i] + prefix_a[n] - prefix_a[i+1])
            else:
                result = min(result, prefix_a[n] - prefix_a[i] + prefix_b[i])
        return result

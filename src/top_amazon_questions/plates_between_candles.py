class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # 2  2 2 5 5 5 9 9 9 9
        #-1 -1 2 2 2 5 5 5 5 9 
        # 0  0 
        n = len(s)
        right = [None] * n
        candle_pos = n
        for i in range(n-1, -1, -1):
            if s[i] == '*':
                right[i] = candle_pos
            else:
                candle_pos = i
                right[i] = candle_pos
        
        left = [None] * n
        candle_pos = -1
        for i in range(n):
            if s[i] == '*':
                left[i] = candle_pos
            else:
                candle_pos = i
                left[i] = candle_pos
        
        # prefx_sum[i] = sum of 0 .. i -1
        prefix = [0] * (n+1)
        for i in range(n):
            if s[i] == '*':
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]
        
        result = []
        for l, r in queries:
            left_most = right[l]
            right_most = left[r]
            if left_most > right_most:
                result.append(0)
            else:
                result.append(prefix[right_most + 1] - prefix[left_most])

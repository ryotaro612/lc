class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        prefix[i] sum(endTime[j] - startTime[j]) j < i

        ---   ---- --- -----   ---
        """
        n = len(startTime)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] += prefix[i] + endTime[i] - startTime[i]

        result = 0
        for i in range(n):
            if i == 0:
                if k < n:
                    result = startTime[k] - prefix[k]
                else:
                    result = eventTime - prefix[n]
                continue
            start = endTime[i-1]
            end = startTime[i+k] if i + k <= n - 1 else eventTime
            
            result = max(result, end - start - (prefix[min(i+k, n)] - prefix[i]))
        return result

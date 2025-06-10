class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        left_array[h] # [i, j] min_len h <= i
        right_array[h]# [i, j) min()  h <= j 
        """
        # left_array[i] + right_array[i+1] -> answer
        n = len(arr)
        left_arr = [float('inf')] * n
        right_arr = [float('inf')] * (n + 1)
        right = 0
        total = 0
        for left in range(n):
            right = max(right, left)
            while right < n and total < target:
                total += arr[right]
                right += 1
            
            if total == target:
                left_arr[left] = min(left_arr[left], right - left)
                right_arr[right] = min(right_arr[right], right - left)
            
            total -= arr[left]
        
        for i in range(n-2, -1, -1):
            left_arr[i] = min(left_arr[i+1], left_arr[i])
        for i in range(1, n+1):
            right_arr[i] = min(right_arr[i-1], right_arr[i])
        #print(left_arr)
        #print(right_arr)
        result = float('inf')

        for i in range(n):
            result = min(result, right_arr[i] + left_arr[i])
        
        return result if result < float('inf') else -1

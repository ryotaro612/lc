class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[i] < stack[-1][0]:
                stack.pop()
            if stack:
                left[i] = stack[-1][1] + 1
            else:
                left[i] = 0
            stack.append([v, i])
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[i] <= stack[-1][0]:
                stack.pop()
            if stack:
                right[i] = stack[-1][1]
            else:
                right[i] = n
            stack.append([arr[i], i])
            
        res = 0
        mod = 10**9 + 7
        for i in range(n):
            res += arr[i] * (i - left[i] + 1) * (right[i] - i)
            res %= mod
        # print(left)
        # rint(right)
        return res

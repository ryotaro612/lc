class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        total = 0
        prefix = [-float('inf')] * n
        for i, num in enumerate(nums):
            total += nums[i]
            if i > k - 1:
                total -= nums[i-k]
            if i >= k-1:
                prefix[i-k + 1] = total
        
        left = [-float('inf')] * n
        left[k-1] = 0
        for i in range(k, n):
            if prefix[i-k+1] > prefix[left[i-1]]:
                left[i] = i-k+1
            else:
                left[i] = left[i-1]
        
        right = [-float('inf')] * n
        right[n-k] = n - k
        for i in range(n-k-1, -1, - 1):
            if prefix[i] >= prefix[right[i+1]]:
                right[i] = i
            else:
                right[i] = right[i+1]
        # print(left, right)
        a, b, c = 0, k, right[k+k]
        for i in range(k+1, n-k-k+1):
            # print(i, left[i-1], right[i+k])
            # print('->', prefix[left[i-1]], prefix[i], prefix[right[i+k]] )
            if prefix[left[i-1]] + prefix[i] + prefix[right[i+k]] > prefix[a] + prefix[b] + prefix[c]:
                a, b, c = left[i-1], i, right[i+k]
        
        return [a, b, c]

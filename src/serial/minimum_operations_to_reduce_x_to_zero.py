"""
[5,2,3,1,1]
3
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        result = n+1
        cur = sum(nums)
        right = 0
        for left in range(n+1):
            while (right < left or cur > x) and right < n:
                cur -= nums[right]
                right += 1
            # print(left, right, cur)
            if left <= right and cur == x:
                result = min(result, left + n - 1 - right + 1)
            if left < n:
                cur += nums[left]
        if result > n:
            return -1
        else:
            return result


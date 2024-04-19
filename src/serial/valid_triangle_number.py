import bisect

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        a, b, c
        a + b > c
        b + c > a
        c + a > b
        """
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        result = 0

        for i in range(n):
            k = i + 2
            for j in range(i+1, n):
                k = max(j+1, k)
                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1
                result += max(0, k - (j+1))

        return result

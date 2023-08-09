class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if not p:
            return 0

        nums = sorted(nums)

        lb, ub = -1, nums[-1] - nums[0] + 1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            if count < p:
                lb = mid
            else:
                ub = mid
        return ub

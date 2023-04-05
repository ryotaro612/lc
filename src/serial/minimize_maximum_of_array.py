class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ub = sum(nums) + 1
        lb = -1
        n = len(nums)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            delta = 0
            ok = True
            for i in range(n-1, -1, -1):
                # print(delta, mid)
                if i > 0:
                    delta = max(0, delta + nums[i] - mid)
                else:
                    if delta + nums[0] > mid:
                        ok = False
            if ok:
                ub = mid
            else:
                lb = mid
        return ub


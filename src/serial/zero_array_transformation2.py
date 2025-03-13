class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        mid = 0

        n = len(nums)
        prefix = [0] * (n+1)
        prefix[i] = sum(nums[:i])
        l, r, val
        dec = [0] * (n + 1)
        dec[l] -= val
        dec[r+1] += val
        """
        n = len(nums)
        n_q = len(queries)
        lb = -1
        ub = n_q + 1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            dec = [0] * (n+1)
            for l, r, val in queries[:mid]:
                dec[l] += val
                dec[r+1] -= val
            for i in range(n):
                dec[i+1] += dec[i]
            ok = True
            for i in range(n):
                if nums[i] > dec[i]:
                    ok = False
            if ok:
                ub = mid
            else:
                lb = mid
                
        if n_q < ub:
            return -1
        return ub

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        ub = 10**10
        lb = 0

        while ub - lb > 1:
            mid = (ub + lb) // 2
            use = 0
            for n1, n2 in zip(nums1, nums2):
                diff = abs(n1 - n2)
                if diff > mid:
                    use += diff - mid

            if use > k1 + k2:
                lb = mid
            else:
                ub = mid

        use = 0
        diffs = []
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            if diff > ub:
                diffs.append(ub)
                use += diff - ub
            else:
                diffs.append(diff)

        diffs.sort(reverse=True)
        for i in range(len(diffs)):
            if diffs[i] and use < k1 + k2:
                diffs[i] -= 1
                use += 1
        
        
        result = 0 
        for diff in diffs:
            result += diff**2
        return result

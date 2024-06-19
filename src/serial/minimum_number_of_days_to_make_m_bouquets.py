class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ub = max(bloomDay) + 1
        lb = 0
        n = len(bloomDay)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            count = 0
            right = 0
            left = 0
            while right < n:
                right = max(left, right)
                if right < n and bloomDay[right] <= mid:
                    right += 1

                if right - left == k:
                    count += 1
                    left = right
                if right < n and mid < bloomDay[right]:
                    left = right + 1
            if count >= m:
                ub = mid
            else:
                lb = mid
                
        if ub == max(bloomDay) + 1:
            return -1
        return ub

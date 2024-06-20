class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ub = position[-1] - position[0] + 1
        lb = 0
        n = len(position)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            prev = -float('inf')
            count = 0
            for i in range(n):
                if position[i] - prev >= mid:
                    count += 1
                    prev = position[i]
            if count >= m:
                lb = mid
            else:
                ub = mid
        return lb

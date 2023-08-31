import heapq

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        not_used = [[i - r, i + r] for i, r in enumerate(ranges)]
        heapq.heapify(not_used)
        available = []
        i = 0
        result = 0
        while i < n:
            while not_used:
                if not_used[0][0] <= i:
                    left, right = heapq.heappop(not_used)
                    heapq.heappush(available, [-right, left])
                else:
                    break
            if available and i <= -available[0][0]:
                neg_right, _ = heapq.heappop(available)
                result += 1
                i = -neg_right
            else:
                return -1
        return result

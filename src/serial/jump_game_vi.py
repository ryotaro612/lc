import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
        nums[i]
        heap (score, j<i)
        (score, i)

        nums[n-1]
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        heap = [(-nums[0], 0)]

        for i in range(1, n):
            while True:
                score, pos = heap[0]
                score = -score
                if i - pos <= k:
                    next_score = nums[i] + score
                    if i == n - 1:
                        return next_score

                    heapq.heappush(heap, (-next_score, i))
                    break
                else:
                    heapq.heappop(heap)
            
            

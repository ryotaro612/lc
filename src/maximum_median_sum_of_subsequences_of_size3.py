from collections import deque
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        que = deque(sorted(nums))
        result = 0
        while que:
            que.popleft()
            que.pop()
            result += que.pop()
        
        return result

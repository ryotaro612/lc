from collections import deque
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        que = deque(sorted(abs(num) for num in nums))
        score = 0
        while que:
            if que:
                item = que.pop()
                score += item * item
            if que:
                item = que.popleft()
                score -= item * item
        
        return score

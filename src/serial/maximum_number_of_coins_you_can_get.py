from collections import deque
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        que = deque(sorted(piles))

        result = 0
        while que:
            que.pop()
            result += que.pop()
            que.popleft()
        return result

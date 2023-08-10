

from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        que = deque(nums)
        while len(que) > 1:
            left, right = que.popleft(), que.pop()
            if left == right:
                continue
            elif left < right:
                que.append(right)
                other = que.popleft()
                que.appendleft(left + other)
            else: # left > right
                que.appendleft(left)
                other = que.pop()
                que.append(other + right)
            result += 1
        return result

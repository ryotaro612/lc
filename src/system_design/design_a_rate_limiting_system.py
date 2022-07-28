"""
["RateLimiter","shouldAllow","shouldAllow","shouldAllow","shouldAllow","shouldAllow"]
[[3,5],[1],[1],[2],[3],[8]]

["RateLimiter","shouldAllow","shouldAllow","shouldAllow"]
[[1,1],[1],[1],[2]]
"""
from collections import deque
class RateLimiter:

    def __init__(self, n: int, t: int):
        self.que = deque()
        self.n = n
        self.t = t

    def shouldAllow(self, timestamp: int) -> bool:
        while len(self.que) > 0:
            ts = self.que.popleft()
            if ts > timestamp - self.t:
                self.que.appendleft(ts)
                break
        if len(self.que) < self.n:
            self.que.append(timestamp)
            return True
        else:
            return False

# Your RateLimiter object will be instantiated and called as such:
# obj = RateLimiter(n, t)
# param_1 = obj.shouldAllow(timestamp)

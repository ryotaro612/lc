# https://leetcode.com/problems/first-unique-number/description/?envType=study-plan-v2&envId=premium-algo-100
from collections import defaultdict


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counter = defaultdict(int)
        self.que = deque()
        for num in nums:
            self.counter[num] += 1
            self.que.append(num)

    def showFirstUnique(self) -> int:
        while self.que:
            if self.counter[self.que[0]] == 1:
                return self.que[0]
            else:
                self.que.popleft()
        return -1

    def add(self, value: int) -> None:
        self.counter[value] += 1
        self.que.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

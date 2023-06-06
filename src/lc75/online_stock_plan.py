"""
["StockSpanner","next","next","next","next","next"]
[[],[31],[41],[48],[59],[79]]
"""


class StockSpanner:
    def __init__(self):
        self.stk = [[100001, 0]]
        self.num = 1

    def next(self, price: int) -> int:
        while self.stk and self.stk[-1][0] <= price:
            self.stk.pop()
        result = self.num - self.stk[-1][1]
        self.stk.append([price, self.num])
        self.num += 1
        return result

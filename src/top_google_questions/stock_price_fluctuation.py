import heapq

class StockPrice:

    def __init__(self):
        self.time = 0
        self.current_stocks = []
        self.max_stocks = []
        self.min_stocks = []
        self.time_price =dict()

    def update(self, timestamp: int, price: int) -> None:
        self.time_price[timestamp] = price
        heapq.heappush(self.current_stocks, (-timestamp, self.time, price))
        heapq.heappush(self.max_stocks, (-price, self.time, timestamp))
        heapq.heappush(self.min_stocks, (price, self.time, timestamp))
        self.time -= 1

    def current(self) -> int:
        return self.current_stocks[0][2]

    def maximum(self) -> int:
        while self.time_price[self.max_stocks[0][2]] != -self.max_stocks[0][0]:
            heapq.heappop(self.max_stocks)
        return -self.max_stocks[0][0]

    def minimum(self) -> int:
        while self.time_price[self.min_stocks[0][2]] != self.min_stocks[0][0]:
            heapq.heappop(self.min_stocks)
        return self.min_stocks[0][0

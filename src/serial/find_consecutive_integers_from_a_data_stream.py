class DataStream:

    def __init__(self, value: int, k: int):
        self.counter = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.counter += 1
            return self.k <= self.counter
        
        self.counter = 0
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

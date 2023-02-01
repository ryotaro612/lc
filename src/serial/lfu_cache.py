import heapq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.history = dict()
        self.heap = []
        self.time = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.touch(key)
            return self.cache[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.touch(key)
            self.cache[key] = value
            return
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
            heapq.heappush(self.heap, (1, self.time, key))
            self.time += 1
        else:
            while self.heap:
                freq, time, cand_key = heapq.heappop(self.heap)
                if cand_key in self.history:
                    heapq.heappush(self.heap, (freq + self.history[cand_key][0], self.history[cand_key][1], cand_key))
                    del self.history[cand_key]
                else:
                    del self.cache[cand_key]
                    self.cache[key] = value
                    heapq.heappush(self.heap, (1, self.time, key))
                    self.time += 1
                    break
                    

    def touch(self, key):
        if key not in self.history:
            self.history[key] = [0, 0]
        self.history[key] = [self.history[key][0] + 1, self.time]
        self.time += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

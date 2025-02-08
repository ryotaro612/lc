import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.idx_num = dict()
        self.num_heap = defaultdict(list)
        self.num_set = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_num:
            old_num = self.idx_num[index]
            self.num_set[old_num].remove(index)
        
        self.idx_num[index] = number
        heapq.heappush(self.num_heap[number], index)
        self.num_set[number].add(index)

    def find(self, number: int) -> int:
        while self.num_set[number]:
            if self.num_heap[number][0] in self.num_set[number]:
                return self.num_heap[number][0]

            heapq.heappop(self.num_heap[number]) 
        
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

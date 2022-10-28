"""
first = [] # i-1th .. 0th
second = [] # ith .. n-1  th

"""
import heapq

class RevName:
    
    def __init__(self, name):
        self.name = name
        
    def __lt__(self, other):
        return self.name > other.name
    
    def __repr__(self):
        return self.name

class SORTracker:

    def __init__(self):
        self.first = []
        self.second = []        
        self.i = 1
        
    def add(self, name: str, score: int) -> None:
        
        if self.first:
            cand_score = self.first[0][0]
            cand_name = self.first[0][1].name
            if cand_score < score or (cand_score == score and name < cand_name):
                heapq.heappop(self.first)
                heapq.heappush(self.first, (score, RevName(name)))
                heapq.heappush(self.second, (-cand_score, cand_name))
            else:
                heapq.heappush(self.second, (-score, name))
        else:
            heapq.heappush(self.first, (score, RevName(name)))
        
        self.balance()
        # print(self.first, self.second)
    def get(self) -> str:
        self.i += 1
        result = self.first[0][1].name
        self.balance()
        return result
        

    def balance(self):
        while self.i <= len(self.first) + len(self.second) and len(self.first) != self.i:
            if len(self.first) < self.i:
                item  = heapq.heappop(self.second)
                heapq.heappush(self.first, (-item[0], RevName(item[1])))
            else:
                item = heapq.heappop(self.first)
                heapq.heappush(self.second, (-item[0], item[1].name))        

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()

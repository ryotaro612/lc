from collections import defaultdict
import random
"""
["RandomizedCollection","insert","remove","insert"]
[[],[1],[1],[1]]

["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
[[],[1],[1],[2],[2],[2],[1],[1],[2],[1],[2],[],[],[],[],[],[],[],[],[],[]]


["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
[[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]
"""
class RandomizedCollection:

    def __init__(self):
        self.items = []
        self.freq = defaultdict(set)

    def insert(self, val: int) -> bool:
        result = val not in self.freq
        self.freq[val].add(len(self.items))
        self.items.append(val)
                    
        return result

    def remove(self, val: int) -> bool:
        # print(val)
        # print(self.freq)
        # print(self.items)
        
        if val not in self.freq:
            return False
        if self.items[-1] == val:
            self.freq[val].remove(len(self.items) - 1)
            self.items.pop()
        else:
            pos = self.freq[val].pop()
            last_value_pos = len(self.items) - 1
            last_value = self.items.pop()
            self.freq[last_value].remove(last_value_pos)
            self.items[pos] = last_value
            self.freq[last_value].add(pos)

        if len(self.freq[val]) == 0:
            del self.freq[val]
        #print('===')
        #print(val)
        #print(self.freq)
        #print(self.items)
        #print('----')
        return True
    
    def getRandom(self) -> int:
        index = random.randrange(0, len(self.items))
        return self.items[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

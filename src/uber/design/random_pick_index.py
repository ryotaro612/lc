import random

class Solution:

    def __init__(self, nums: List[int]):
        num_index = dict()
        for i, num in enumerate(nums):
            num_index.setdefault(num, [])
            num_index[num].append(i)
        self.num_index = num_index
        
    def pick(self, target: int) -> int:
        index =self.num_index[target]
        return index[random.randrange(0, len(index))]        

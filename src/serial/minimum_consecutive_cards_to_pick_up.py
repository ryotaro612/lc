import math
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        val_pos = defaultdict(list)
        for i, card in enumerate(cards):
            val_pos[card].append(i)
        
        result = math.inf
        for index in val_pos.values():
            n = len(index)
            for i in range(n - 1):
                result = min(result, index[i+1] - index[i] + 1)
        
        return result if math.inf > result else -1

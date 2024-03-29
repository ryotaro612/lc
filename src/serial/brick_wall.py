from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq = defaultdict(int)
        for row in wall:
            prefix_sum = 0
            freq[0] += 1
            for cell in row:
                prefix_sum += cell
                freq[prefix_sum] += 1
        
        n_rows = len(wall)
        if len(freq) == 2:
            return n_rows
        del freq[0]
        del freq[max(freq.keys())]
        return n_rows - max(freq.values())

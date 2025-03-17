class Bit:

    def __init__(self, size):
        self.bit = [0] * (size + 1)
    
    def add(self, i, v):
        i += 1
        while i < len(self.bit):
            self.bit[i] += v
            i += i & -i
    
    def sum(self, i):
        result = 0
        while i:
            result += self.bit[i]
            i -= i & -i
        return result

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        bit = Bit(2*m)
        pos = {}
        for i in range(m):
            bit.add(m+i, 1)
            pos[i+1] = m+i
        
        result = []
        for i, q in enumerate(queries):
            p = pos[q]
            result.append(bit.sum(p+1))
            bit.add(p, -1)
            bit.add(m-1-i, 1)
            pos[q] = m-1-i
        
        return [r - 1 for r in result]

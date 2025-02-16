class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [None] * (2*n-1)
        cands = {i for i in range(1, n+1)}

        self.rec(cands, result)
        return result
    
    def rec(self, cands, result):
        if not cands:
            return True
        
        order = sorted(list(cands), reverse=True)
        
        for pos in range(len(result)):
            if result[pos] is None:
                break
        
        for v in order:
            if v == 1:
                result[pos] = v
                if self.rec(cands - {v}, result):
                    return True
                result[pos] = None
            elif pos + v < len(result) and result[pos] is None and result[pos+v] is None:
                result[pos] = v
                result[pos + v] = v
                if self.rec(cands - {v}, result):
                    return True
                result[pos] = None
                result[pos + v] = None
        
        return False

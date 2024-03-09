class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        result = -1
        n = len(strs)
        for i, s in enumerate(strs):
            subseqs = self.find(s)
            # print(subseqs, s)
            for subseq in subseqs:
                for j in range(n):
                    if i != j and self.is_subseq(subseq, strs[j]):
                        break
                else:
                    result = max(result, len(subseq))
        return result
    
    def find(self, s):
        results  = [[]]
        self._find(0, s, results)
        return [''.join(result) for result in results if result]
    
    def _find(self, i, s, results):
        n = len(s)
        if i == n:
            return
        temp = [list(result) for result in results]
        for cand in temp:
            cand.append(s[i])
        results.extend(temp)
        self._find(i+1, s, results)

    def is_subseq(self, cand, s):
        i = 0
        for c in s:
            if cand[i] == c:
                i+= 1
            if i == len(cand):
                return True
        return False

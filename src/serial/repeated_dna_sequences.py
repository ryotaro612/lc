from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = defaultdict(int)
        n = len(s)
        result = []
        for i in range(n):
            seq = s[i:i+10]
            if len(seq) == 10:
                freq[seq] += 1
                if freq[seq] == 2:
                    result.append(seq)
        return result

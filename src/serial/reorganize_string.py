class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        result = []
        while len(result) < len(s):
            cand = -1 
            for i in range(26):
                if letters[i] and (len(result) == 0 or (result and result[-1] != i)):
                    if cand == -1 or letters[i] > letters[cand]:
                        cand = i
            if cand == -1:
                return ""
            else:
                result.append(cand)
                letters[cand] -= 1

        return "".join([chr(i + ord('a')) for i in result])
            

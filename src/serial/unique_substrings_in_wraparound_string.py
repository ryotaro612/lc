class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        letters = [0] * 26
        count = 0
        res = 0
        for i, c in enumerate(s):
            c_i = ord(c) - ord('a')
            if i:
                if ord(s[i-1]) - ord('a') == (c_i - 1 + 26) % 26:
                    count += 1
                else:
                    count  = 1
            else:
                count += 1
            
            res += max(0, count - letters[c_i])
            letters[c_i] = max(letters[c_i], count)
        return res

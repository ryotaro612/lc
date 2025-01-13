class Solution:
    def minimumLength(self, s: str) -> int:
        lst = [[] for _ in range(26)]
        for i, c in enumerate(s):
            lst[ord(c) - ord('a')].append(i)
        
        result = 0
        for i in range(26):
            while len(lst[i]) >= 3:
                lst[i].pop()
                lst[i].pop()
            result += len(lst[i])
        return result

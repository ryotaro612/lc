"""
(n, 2) -> O(n^2)
"ABC"
pos['A'] = [0] -> [-1, 0, 3]
pos['B'] = [1]
pos['C'] = [2]
"""
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos = [[-1] for _ in range(26)]
        for i, c in enumerate(s):
            key = ord(c) - ord('A')
            pos[key].append(i)
        n = len(s)
        
        result = 0
        for i in range(26):
            pos[i].append(n)
            for j in range(1, len(pos[i])-1):
                left = pos[i][j] - pos[i][j-1]
                right = pos[i][j+1] - pos[i][j]
                result += left * right
        return result

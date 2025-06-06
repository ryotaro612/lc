from collections import deque
class Solution:
    def robotWithString(self, s: str) -> str:
        """
        a, i, b, j i < j
        """
        n = len(s)
        smaller = ['z'] * n
        smaller[-1] = s[-1]
        for i in range(n-2, -1, -1):
            smaller[i] = min(s[i], smaller[i+1])
        
        stack = []
        paper = []
        for i, c in enumerate(s):
            stack.append(c)
            while i < n-1 and stack and stack[-1] <= smaller[i+1]:
                paper.append(stack.pop())
            
        
        while stack:
            paper.append(stack.pop())
        
        return ''.join(paper)

        #smapper[i] < j

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        required = [True] * len(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))
            elif c == ")":
                if len(stack) == 0:
                    required[i] = False
                else:
                    stack.pop()
        while 0 < len(stack):
            _, i = stack.pop()
            required[i] = False
        
        return ''.join([c for c, b in zip(s, required) if b])

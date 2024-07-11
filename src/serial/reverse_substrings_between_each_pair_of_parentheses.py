class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                poped = []
                while stack[-1] != '(':
                    poped.append(stack.pop())
                stack.pop()
                stack.extend(poped)
            else:
                stack.append(c)
        return ''.join(stack)

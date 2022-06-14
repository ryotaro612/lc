"""
" 3+5 / 2 / 2 - 1"
"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                operand *= 10
                operand += int(c)
            elif c in {'+', '-'}:
                operand = self.consume_md(stack, operand)
                operand = self.consume_pm(stack, operand)
                stack.append((operand, c))
                operand = 0
            elif c in {'*', '/'}:
                operand = self.consume_md(stack, operand)
                stack.append((operand, c))
                operand = 0
            else:
                assert False
        
        operand = self.consume_md(stack, operand)
        return self.consume_pm(stack, operand)
                
    def consume_pm(self, stack, operand):
        #print(stack, operand)
        while stack:
            left, op = stack.pop()
            if op == '+':
                operand += left
            elif op == '-':
                operand = left - operand
        return operand
    
    def consume_md(self, stack, operand):
        # print(stack, operand)
        while stack and stack[-1][1] in {'*', '/'}:
            left, op = stack.pop()
            if op == '*':
                operand = left * operand
            else:
                operand = left // operand
        return operand

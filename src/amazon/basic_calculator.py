class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        level = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num *= 10
                num += int(c)
            elif c in {'-', '+'}:
                if stack and stack[-1][2] == level and stack[-1][1] in {'*', '/'}:
                    left, op, _ = stack.pop()
                    num = self.compute(left, num, op)
                stack.append((num, c, level))
                num = 0
            elif c in {'*', '/'}:
                stack.append((num, c, level))
                num = 0
            elif c == '(':
                level += 1
            elif c == ')':
                while stack and stack[-1][2] == level:
                    left, op, _ = stack.pop()
                    num = self.compute(left, num, op)                        
                level -= 1
            else:
                assert False
        while stack:
            left, op, level = stack.pop()
            assert level == 0
            num = self.compute(left, num, op)
        return num
    
    def compute(self, left, right, op):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return self.div(left, right)
        else:
            assert False
                
    def div(self, left, right):
        if left * right >= 0:
            return left // right
        
        return -(abs(left) // abs(right))
            

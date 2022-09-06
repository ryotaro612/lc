"""
"1+1"
"6-4/2"
"6*2-5+(54*2)/3*4+4-23"
"23+(4-3/2)+(2*(5-(23)+2/2+(0)))"
"23+(4-3/2*(24+(5*12-3)))+(2*(5-(23)+2/2+(0)))"

"(2+6*3+5-(3*14/7+2)*5)+3"
"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        level = 0
        for i in range(len(s)):
            #print(num, stack)
            c = s[i]
            if c.isdigit():
                num *= 10
                num += int(c)
            elif c in {'-', '+', '*', '/'}:
                num = self.compute_muldiv(stack, num, level)
                stack.append((num, c, level))
                num = 0
            elif c == '(':
                level += 1
            elif c == ')':
                num = self.compute_muldiv(stack, num, level)
                num = self.compute_pn(stack, num, level)                      
                level -= 1
            else:
                assert False
        #print(num, stack)
        num = self.compute_muldiv(stack, num, level)
        num = self.compute_pn(stack, num, level)
        return num
    
            
    def compute_muldiv(self, stack, right, level):
        if stack and stack[-1][2] == level and stack[-1][1] in {'*', '/'}:
            left, op, _ = stack.pop()
            return self.compute(left, right, op)
        else:
            return right
        
    def compute_pn(self, stack, right, level):
        temp = [(right, '+', level)]
        while stack and stack[-1][2] == level:
            temp.append(stack.pop())
        
        result = 0
        op = '+'
        #print('temp', temp)
        while temp:
            left, next_op, _ = temp.pop()
            if op == '+':
                result += left
            elif op == '-':
                result -= left
            else:
                assert False
            op = next_op
        return result

    def compute(self, left, right, op):
        if op == '+':
            return left + right
        if op == '-':
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
            

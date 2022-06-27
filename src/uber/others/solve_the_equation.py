"""
"x+5-3+x=6+x-2"
"2x=x"
"x=x"
"2x+4=2"
"4=2-2x"
"0x=0"
"""
class Solution:
    def solveEquation(self, equation: str) -> str:
        exprs = equation.split('=')
        left, right = self.compute(exprs[0]), self.compute(exprs[1])
        # print(left, right)
        if left == right:
            return "Infinite solutions"

        x_coeff = left[1] - right[1]
        v  = right[0] - left[0]
        # print(x_coeff, v)
        if x_coeff == 0:
            return "No solution"
        x = v // x_coeff
        
        return f"x={x}"
    
    def compute(self, expr: str):
        acc = (0, 0)
        op = '+'
        v = (0, 0)
        n = len(expr)
        
        for i in range(n):
            c = expr[i]
            if c.isdigit():
                v = (10 * v[0] + int(c), v[1])
            elif c == 'x':
                if v[0] == 0:
                    if i > 0 and expr[i-1] == '0':
                        v = (0, 0)
                    else:
                        v = (0, 1)
                else:
                    v = (0, v[0])
                    
            if c in {'+', '-'} or i == n-1:
                if op == '+':
                    acc = (acc[0] + v[0], acc[1] + v[1])
                elif op == '-':
                    acc = (acc[0] - v[0], acc[1] - v[1])
                else:
                    assert False
                op = c
                v = (0, 0)
        return acc

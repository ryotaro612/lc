"""
"(1-23-4)"
"-2+ 1"
"- (3 + (4 + 5))"
"""
class Solution:
    def calculate(self, s: str) -> int:
        s = self.normalize(s)
        return self.calc(s)
    
    def calc(self, s):
        res = 0
        op_stack, res_stack = [], []
        operand = 0
        sign = 1
        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
            
            elif c == '+':
                res += operand * sign
                sign = 1
                operand = 0
            elif c == '-':
                res += operand * sign
                sign = -1
                operand = 0
            elif c == '(':
                op_stack.append(sign)
                res_stack.append(res)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * operand
                res *= op_stack.pop()
                
                res += res_stack.pop()
                operand = 0
            else:
                print('#', c, c.isdigit())
                assert False
        res += operand * sign
        return res
        
    def normalize(self, s):
        return ''.join([c for c in s if c != ' '])
    
"""
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand
"""

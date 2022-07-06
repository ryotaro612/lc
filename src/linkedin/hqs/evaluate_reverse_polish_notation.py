class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(stack)
            if token == '+':
                right, left = stack.pop(), stack.pop()
                stack.append(left + right)
            elif token == '-':
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif token == '*':
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)
            elif token == '/':
                right, left = stack.pop(), stack.pop()
                stack.append(self.div(left, right))
            else:
                stack.append(int(token))
        return stack[-1]
    
    def div(self, left, right):
        result = abs(left) // abs(right)
        if left * right >= 0:
            return result
        else:
            return -result

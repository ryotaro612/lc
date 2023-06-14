class Solution:
    def parseTernary(self, expression: str) -> str:
        return self.eval(expression, 0)[0]

    def eval(self, expr, pos):
        if pos != len(expr) - 1 and expr[pos + 1] == "?":
            left, next_pos = self.eval(expr, pos + 2)
            right, next_pos = self.eval(expr, next_pos + 1)
            if expr[pos] == "T":
                return left, next_pos
            else:
                return right, next_pos
        else:
            return expr[pos], pos + 1

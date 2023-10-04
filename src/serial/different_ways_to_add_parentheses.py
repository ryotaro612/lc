class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = dict()
        return self.calc(expression, cache)

    def calc(self, expr, cache):
        if expr in cache:
            return cache[expr]
        n = len(expr)
        for i in range(n):
            if expr[i] in {'+', '-', '*'}:
                break
            if i == n-1:
                cache[expr] = [int(expr)]
                return cache[expr]
        result = []
        for i in range(n):
            if expr[i] in {'+', '-', '*'}:
                left = self.calc(expr[:i], cache)
                right = self.calc(expr[i+1:], cache)
                for left_e in left:
                    for right_e in right:
                        if expr[i] == '+':
                            res = left_e + right_e
                        elif expr[i] == '-':
                            res = left_e - right_e
                        else:
                            res = left_e * right_e
                        
                        result.append(res)
        cache[expr] = result
        return cache[expr] 

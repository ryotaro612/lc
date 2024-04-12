class Solution:
    def fractionAddition(self, expression: str) -> str:
        acc = [0, 1]
        left, right = 0, 1
        if expression[0] != '-':
            expression = '+' + expression
        
        n = len(expression)
        while left < n:
            fraction = []
            while right < n and expression[right] not in {'+', '-'}:
                fraction.append(expression[right])
                right += 1
            

            l_expr, r_expr = ''.join(fraction).split('/')
            l_int, r_int = int(l_expr), int(r_expr)
            if expression[left] == '-':
                l_int *= -1
            acc = self.reduce(self.add(acc, [l_int, r_int]))

            left = right
            right += 1
        
        return str(acc[0]) + '/' + str(acc[1])
    
    def add(self, a, b):
        a_nume, a_denom = a
        b_nume, b_denom = b

        return [a_nume*b_denom + b_nume*a_denom, a_denom * b_denom]

    def reduce(self, acc):
        nume, denom = acc

        while self.gcd(abs(nume), abs(denom)) > 1:
            g = self.gcd(abs(nume), abs(denom))
            nume //= g
            denom //= g
        
        return [nume, denom]

    
    def gcd(self, a, b):
        if b > a:
            return self.gcd(b, a)
        if b == 0:
            return a
        return self.gcd(b, a % b)

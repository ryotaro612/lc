class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        n1 = len(str1)
        i = 1
        divisors = []
        while i * i <= n1:
            if n1 % i == 0:
                divisors.append(i)
                if n1 // i != i:
                    divisors.append(n1 // i)
            i+= 1
        divisors.sort(reverse=True)
        for divisor in divisors:
            s = str1[:divisor]
            if self.div(str1, s) and self.div(str2, s):
                return s
        return ''

    def div(self, s, d):
        nd = len(d)
        n = len(s)
        if n % nd != 0:
            return False
        for i in range(0, n, nd):
            if s[i:i+nd] != d:
                return False
        return True

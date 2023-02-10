class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        divisors= self.find_divisors(n)
        divisors.pop()
        for divisor in divisors:
            ok = True
            for j in range(divisor, n, divisor):
                if s[:divisor] != s[j:j+divisor]:
                    ok = False
                    break
            if ok:
                return True
        return False

    def find_divisors(self, n):
        divisors = set()
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
            i += 1
        return sorted(divisors)

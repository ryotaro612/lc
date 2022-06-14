"""
"1234567"
"123456"
"123"
"1"
"99"
"993"
"1000"
"10000"
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n) <= 10:
            return str(int(n) - 1)
    
        result = self.compute_palindrome(n)
        if result == n:
            result = '9'
        # print(result, 'palindrome')
        cand = self.compute_large(n)
        # print(cand)
        if abs(int(n) - int(cand)) < abs(int(n) - int(result)):
            result = cand
        elif abs(int(n) - int(cand)) == abs(int(n) - int(result)):
            if int(cand) < int(result):
                result = cand

        cand = self.compute_less(n)
        # print(cand)
        if abs(int(n) - int(cand)) < abs(int(n) - int(result)):
            result = cand
        elif abs(int(n) - int(cand)) == abs(int(n) - int(result)):
            if int(cand) < int(result):
                result = cand
        return result 
    
    def compute_palindrome(self, s):
        n = len(s)
        half = s[:n//2]
        if n % 2 == 1:
            return half + s[n//2] + half[::-1]
        return half + half[::-1]
    
    def compute_less(self, s):
        n = len(s)
        half = s[:n//2]
        if n % 2 == 1:
            mid = s[n // 2]
            half_dec = str(int(half + mid) - 1)
            if len(half + mid) == len(half_dec):
                return half_dec[:-1] + half_dec[-1] + half_dec[:-1][::-1]
            else:
                return '9' * (n-1)
        else:
            half_dec = str(int(half) - 1)
            if len(half) == len(half_dec):
                return half_dec + half_dec[::-1]
            else:
                return '9' * (n-1)
    
    def compute_large(self, s):
        n = len(s)
        half = s[:n//2]
        if n % 2 == 1:
            mid = s[n // 2]
            half_inc = str(int(half + mid) + 1)
            if len(half + mid) == len(half_inc):
                return half_inc[:-1] + half_inc[-1] + half_inc[:-1][::-1]
            else:
                return '1' + '0' * (n-1) + '1'
        else:
            half_inc = str(int(half) + 1)
            if len(half) == len(half_inc):
                return half_inc + half_inc[::-1]
            else:
                return '1' + '0' * (n-1) + '1'

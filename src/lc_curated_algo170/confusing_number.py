class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = list(str(n))
        rev_s = s[::-1]
        conv = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        for i in range(len(rev_s)):
            if rev_s[i] in conv:
                rev_s[i] = conv[rev_s[i]]
            else:
                return False
        
        return rev_s != s

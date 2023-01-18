class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        i, j = n1-1, n2-1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            if i >=0:
                d1 = ord(num1[i]) - ord('0')
            else:
                d1 = 0
            if j >=0:
                d2 = ord(num2[j]) - ord('0')
            else:
                d2 = 0
 
            d = d1 + d2 + carry
            carry = d // 10
            result.append(chr(d % 10 + ord('0')))
            i -= 1
            j -= 1
        if carry:
            result.append(chr(carry + ord('0')))
        return ''.join(result[::-1])

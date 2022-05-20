class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0:
            av, bv = 0, 0            
            if i >= 0:
                av = int(a[i])
            if j >= 0:
                    bv = int(b[j])

            temp = carry + av + bv
            carry = temp // 2
            result.append(str(temp % 2))
            i -= 1
            j -= 1
        if carry > 0:
            result.append(str(carry))
        return ''.join(reversed(result))

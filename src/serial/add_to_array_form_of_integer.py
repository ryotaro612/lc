"""
[9,9,9,9,9,9,9,9,9,9]
1
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        k = [int(c) for c in str(k)][::-1]
        carry = 0
        n_num = len(num)
        n_k = len(k)
        result = []
        for i in range(max(n_num, n_k)):
            a, b = 0, 0
            if i < n_num:
                a = num[i]
            if i < n_k:
                b = k[i]

            result.append( (a + b + carry) % 10)
            carry = (a + b + carry) // 10
        if carry:
            result.append(1)

        return result[::-1] 

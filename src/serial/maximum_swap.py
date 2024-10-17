class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [c for c in str(num)]
        for i in range(len(digits)):
            mx = int(digits[i])
            mx_i = -1
            for j in range(len(digits)-1, i, -1):
                if mx < int(digits[j]):
                    mx = int(digits[j])
                    mx_i = j
            
            if mx_i >= 0:
                digits[i], digits[mx_i] = digits[mx_i], digits[i]

                return int(''.join(digits))
        
        return num

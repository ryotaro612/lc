"""
1
2

2
1

4
333

1
6

-50
8
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:
            sign = '-'
        else:
            sign = ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_quotient  = sign + str(numerator // denominator)
        remainder = numerator % denominator     
        if remainder == 0:
            return int_quotient
        int_quotient += '.'
        decimals = []
        remainders = dict()
        while True:
            remainder *= 10
            if remainder == 0:
                return int_quotient + ''.join(decimals) 
            elif remainder in remainders:
                loop_start = remainders[remainder]
                return int_quotient + ''.join(decimals[:loop_start]) + '(' + ''.join(decimals[loop_start:]) + ')'

            remainders[remainder] = len(decimals)
            decimals.append(str(remainder // denominator))
            remainder %= denominator

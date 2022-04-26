"""
-2147483648
-1
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0 and 0 < divisor) or (0 < dividend and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while divisor <= dividend:
            num_shift = 0
            while (divisor << (num_shift + 1)) <= dividend:
                num_shift += 1
            dividend -= divisor << num_shift
            quotient += 1 << num_shift
        if not is_negative and (2 ** 31 - 1) < quotient:
            return (2 ** 31) - 1
        if is_negative and (2 ** 31) < quotient:
            return -(2 ** 31)
        return -quotient if is_negative else quotient

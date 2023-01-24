class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i *= 2
        return ~num & (i-1)

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        x = 0
        for i in range(n-1, -1, -1):
            mask = 1 << i
            if ((a & mask) == 0) and ((b & mask) == 0):
                a |= mask
                b |= mask
            if (a & mask) and ((b & mask) == 0):
                if a > b:
                    a ^= mask
                    b |= mask
            if ((a & mask) == 0) and (b & mask):
                if a < b:
                    a|= mask
                    b ^= mask
        mod = 10**9 + 7
        return a * b % mod

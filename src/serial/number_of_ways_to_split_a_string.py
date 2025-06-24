class Solution:
    def numWays(self, s: str) -> int:

        n = len(s)
        pos_ones = [i for i, c in enumerate(s) if c == '1']
        n_ones = len(pos_ones)
        if n_ones % 3:
            return 0
        
        mod = 10**9 + 7
        if n_ones == 0:
            return (n-1) * (n-2) // 2 % mod
        
        # 110110011 [0, 1, 3, 4, 7, 8] m = 2, k = 3
        m = pos_ones[n_ones//3] - pos_ones[n_ones//3-1]
        k = pos_ones[n_ones//3*2] - pos_ones[n_ones//3*2 -1]

        return m * k % mod

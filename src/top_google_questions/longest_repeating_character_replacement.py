class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        prfix[i][j] = num of the jth letter from s[0:j]
        range(a, b)
        prefix[b][j] - prefix[a][j]

        0 <= j <= 25
        0 <= i <= len(s)
        prefix[i] 
        """
        n = len(s)
        prefix = [[0] * 26 for _ in range(n+1)]
        for i, c in enumerate(s):
            for j in range(26):
                prefix[i+1][j] += prefix[i][j]
            
            prefix[i+1][ord(c) - ord('A')] += 1

        ub = n + 1
        lb = 0
        while ub - lb > 1:
            mid = (ub + lb) // 2
            ok = False

            i = 0
            while i + mid <= n:
                max_freq = 0
                for j in range(26):
                    max_freq = max(max_freq, prefix[i+mid][j] - prefix[i][j])
                if mid - max_freq <= k:
                    ok = True
                i += 1
            if ok:
                lb = mid
            else:
                ub = mid
        return lb

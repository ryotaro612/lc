import bisect

class Solution:
    def balancedString(self, s: str) -> int:
        """
        prefix[i] - prefix[j] sum of elements between i:j
        """
        n = len(s)
        prefix = [[0] * (n+1) for _ in range(4)]
        mp = {'Q': 0, 'W': 1, 'E': 2, 'R': 3}

        for i, c in enumerate(s):
            for j in range(4):
                prefix[j][i+1] = prefix[j][i]
            prefix[mp[c]][i+1] += 1
        
        result = n
        for i, c in enumerate(s):
            ub = n + 1
            lb = i - 1
            while ub - lb > 1:
                mid = (ub + lb) // 2
                ok = True
                for j in range(4):
                    if prefix[j][n] - (prefix[j][mid] - prefix[j][i]) > n // 4:
                        ok = False
                if ok:
                    ub = mid
                    result = min(result, ub - i)
                else:
                    lb = mid
            
        return result

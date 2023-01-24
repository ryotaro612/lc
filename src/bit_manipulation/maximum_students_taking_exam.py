"""
[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]

[[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]
 
[["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]

[[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],["#",".",".",".",".","#","#","."],[".",".",".",".",".","#",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".","#",".","."],["#",".",".",".",".",".",".","#"]]
"""
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n_col = len(seats[0])
        dp = [-float('inf')] * (1 << n_col)
        dp[0] = 0
        for col in seats:
            next_dp = [-float('inf')] * (1 << n_col)
            
            mask = 0
            for i in range(n_col):
                if col[i] == '#':
                    mask |= (1 << i)
            mask = ~mask
            
            for i in range(1 << n_col):
                if dp[i] < 0:
                    continue
                for j in range(1 << n_col):
                    j &= mask
                    temp = 0
                    for k in range(n_col):
                        if j & (1 << k):
                            ok = True
                            if k < n_col - 1 and (j & (1 << (k+1)) or i & (1 << (k+1))):
                                ok = False
                            if k > 0 and (j & (1 << (k-1)) or i & (1 << (k-1))):
                                ok = False
                            if ok:
                                temp += 1
                    next_dp[j] = max(next_dp[j], temp + dp[i])
            dp = next_dp
        result = max(dp)
        if result > -float('inf'):
            return result
        else:
            return 0
                            

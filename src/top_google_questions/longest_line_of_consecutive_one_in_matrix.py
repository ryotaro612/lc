"""
[[0,1,0,1,1],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]
 """

Accepted
an hour ago
Python3
Wrong Answer
an hour ago
Python3
Close
nryotaro
nryotaro
Apr 24, 2023 12:04

Details
Solution
Python3
Runtime
417 ms
Beats
83.68%
Memory
16.5 MB
Beats
84.94%
Click the distribution chart to view more details
Notes
Write your notes here
Related Tags
Select tags
0/5
"""
[[0,1,0,1,1],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]

 [[1,1,0,1],
  [0,0,1,0],
  [0,1,0,0]]

[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
 """
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        n_row = len(mat)
        n_col = len(mat[0])
        dp = [[0] * 4 for _ in range(n_col + 2)]
        prev = [[0] * 4 for _ in range(n_col + 2)]
        result = 0
        for r in range(n_row-1, -1, -1):
            for c in range(n_col-1, -1, -1):
                if mat[r][c] == 0:
                    dp[c+1] = [0, 0, 0, 0]
                else:
                    dp[c+1] = [1, 1, 1, 1]
                    dp[c+1][0] += dp[c+2][0]
                    dp[c+1][1] += prev[c+1][1]
                    dp[c+1][2] += prev[c+2][2]
                    dp[c+1][3] += prev[c][3]
                    
                    result = max(result, max(dp[c+1]))
            
            dp, prev = prev, dp
        
        return result
"""
    class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        n_row = len(mat)
        n_col = len(mat[0])
        dp = [[[0, 0, 0] for _ in range(n_col+1)] for _ in range(n_row+1)]

        result = 0
        for r in range(n_row-1, -1,-1):
            for c in range(n_col-1, -1,-1):
                if mat[r][c] == 1:
                    dp[r][c] = [1, 1, 1]
                    dp[r][c][0] += dp[r+1][c][0]
                    dp[r][c][1] += dp[r][c+1][1]
                    dp[r][c][2] += dp[r+1][c+1][2]

                result = max(result, max(dp[r][c]))

                # print(r, c, '->', dp[r][c])
        anti_dp = [[0] * n_col for _ in range(n_row)]

        for r in range(n_row-1, -1,-1):
            for c in range(n_col):
                if mat[r][c] == 1:
                    anti_dp[r][c] = 1
                    if c and r != n_row - 1:
                        anti_dp[r][c] += anti_dp[r+1][c-1]

                result = max(result, anti_dp[r][c])
        
        return result
"""

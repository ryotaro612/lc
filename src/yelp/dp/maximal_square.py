"""
  dp[i] = the number of consecutive 1 from the left side
  n_row = n
  n_col = m
  dp[0-n_row]
  dp[0] = 0
  dp[1] = 2
  dp[2] = 3
  dp[3] = 1
  O(n*m + n * n * m)
  
     0   1   2  [3]  4
0 [["1","0","1","0","0"],
1  ["1","0","1","1","1"],
2  ["1","1","1","1","1"],
3  ["1","0","0","1","0"]
 ]
 
 
 [["0","1"],["1","0"]]
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        result = 0
        height = [0] * n_col
        left = [0] * n_col
        right = [n_col] * n_col
        
        for i in range(n_row):
            cur_left = 0
            cur_right = n_col
            for j in range(n_col):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n_col):
                if matrix[i][j] == '1':
                    left[j] = max(cur_left, left[j])
                else:
                    left[j] = 0
                    cur_left = j +1 
            for j in reversed(range(n_col)):
                if matrix[i][j] == '1':
                    right[j] = min(cur_right, right[j])
                else:
                    right[j] = n_col
                    cur_right = j
            for j in range(n_col):
                edge = min(height[j], right[j] - left[j])
                result = max(result, edge * edge)
            
        return result

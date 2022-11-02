"""
d[rowIndex]
len(d[rowIndex]) == rowIndex + 1

d[rowIndex][i] = 1 if i == 0 or i == rowIndex else d[rowIndex-1][i-1] + dp[rowIndex-1][i]
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for i in range(1, rowIndex+1):
            next_row = [1] * (i+1)
            
            for j in range(1, i):
                next_row[j] = row[j-1] + row[j]
            
            row = next_row
        
        return row
        

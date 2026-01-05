class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        mini = float('inf')
        total = 0
        count = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] < 0:
                    count += 1
                mini = min(abs(matrix[r][c]), mini)
                total += abs(matrix[r][c])
        
        if count % 2:
            return total - mini * 2
        else:
            return total
        

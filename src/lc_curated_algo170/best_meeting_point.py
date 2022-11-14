class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        
        row_count = [0] * n_row
        col_count = [0] * n_col
        row_cost = 0
        col_cost = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1
                    row_cost += i
                    col_cost += j
        
        total_row = sum(row_count)
        up_count = row_count[0]
        running_row_cost = row_cost
        # print(running_row_cost)
        for i in range(1, n_row):
            running_row_cost += up_count
            running_row_cost -= total_row - up_count
            # print(running_row_cost)
            row_cost = min(running_row_cost, row_cost)
            
            up_count += row_count[i]
            
        total_col = sum(col_count)
        left_count = col_count[0]
        running_col_cost = col_cost
        for i in range(1, n_col):
            running_col_cost += left_count
            running_col_cost -= total_col - left_count
            
            col_cost = min(col_cost, running_col_cost)
            
            left_count += col_count[i]
            
        return col_cost + row_cost

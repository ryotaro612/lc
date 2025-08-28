class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        grid[0][c], grid[1][c+1]..grid[0+i][c+i]
        1 <= c <n_cols - 1
        grid[r][0]
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        for c in range(1, n_cols):
            arr = []
            i = 0
            while i < n_rows and c + i < n_cols:
                arr.append(grid[i][c+i])
                i += 1
            arr.sort()
            i = 0
            while i< n_rows and c + i < n_cols:
                grid[i][c+i] = arr[i]
                i += 1
        
        for r in range(n_rows):
            arr = []
            i = 0
            while r + i < n_rows and i < n_cols:
                arr.append(grid[r+i][i])
                i += 1
            arr.sort(reverse=True)
            i = 0
            while r + i < n_rows and i < n_cols:
                grid[r+i][i] = arr[i]
                i+=1
        
        return grid

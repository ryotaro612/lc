class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n_rows = len(boxGrid[0])
        n_cols = len(boxGrid)
        grid = [['.'] * n_cols for _ in range(n_rows)]
        for r in range(len(boxGrid)):
            for c in range(len(boxGrid[0])):
                column = n_cols - 1 - r
                row = c
                grid[row][column] = boxGrid[r][c]
        
        for c in range(n_cols):
            lst = [r for r in range(n_rows) if grid[r][c] == '#' or grid[r][c] == '*']
            if not lst:
                continue
            
            d_r = n_rows - 1
            while lst:
                r = lst.pop()
                if grid[r][c] == '*':
                    d_r = r-1
                else:
                    grid[r][c] = '.'
                    grid[d_r][c] = '#'
                    d_r -= 1
        
        return grid

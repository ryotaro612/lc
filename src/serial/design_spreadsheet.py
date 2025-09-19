class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        r, c = self.get_idx(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        if formula[0] == '=':
            left, right = formula[1:].split('+')
            return self.getValue(left) + self.getValue(right)
        
        if formula[0].isupper():
            r, c = self.get_idx(formula)
            return self.grid[r][c]
        
        return int(formula)

    def get_idx(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1        
        return row, col
    
    
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

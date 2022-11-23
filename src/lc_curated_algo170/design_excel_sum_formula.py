"""
["Excel","set","set","sum","sum"]
[[26,"Z"],[1,"A",1],[1,"I",1],[7,"D",["A1:D6","A1:G3","A1:C12"]],[10,"G",["A1:D7","D1:F10","D3:I8","I1:I9"]]]
"""
class Excel:

    def __init__(self, height: int, width: str):
        self.mat = [[lambda: 0] * (self.alpha_to_int(width) + 1) for _ in range(height)]
        
    def set(self, row: int, column: str, val: int) -> None:
        r = row - 1
        c = self.alpha_to_int(column)
        self.mat[r][c] = lambda: val

    def get(self, row: int, column: str) -> int:
        r = row - 1
        c = self.alpha_to_int(column)
        return self.mat[r][c]()

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r = int(row) - 1
        c = self.alpha_to_int(column)
        
        orders = [d for number in numbers for d in self.decode(number)]
        self.mat[r][c] = lambda: self.sum_cells(orders)
        return self.mat[r][c]()
    
    def alpha_to_int(self, alpha):
        return ord(alpha) - ord('A')


    def sum_cells(self, cells):
        result = 0
        for r, c in cells:
            result += self.mat[r][c]()
        
        return result
    
    def decode(self, number: str):
        idx = number.find(':')
        if idx == -1:
            r = int(number[1:]) - 1
            c = self.alpha_to_int(number[0])
            return [[r, c]]
        else:
            tl_r = int(number[1:idx]) - 1
            tl_c = self.alpha_to_int(number[0])
            br_r = int(number[idx+2:]) - 1
            br_c = self.alpha_to_int(number[idx+1])
            
            result = []
            for r in range(tl_r, br_r + 1):
                for c in range(tl_c, br_c+1):
                    result.append([r, c])
            # print(number, result)
            return result
        
# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

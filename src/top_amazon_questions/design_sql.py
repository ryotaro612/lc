class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = dict()
        self.ids = dict()
        for name in names:
            self.tables[name] = dict()
            self.ids[name] = 1
    def insertRow(self, name: str, row: List[str]) -> None:
        table = self.tables[name]
        key = self.ids[name]
        self.ids[name] += 1
        table[key] = row


    def deleteRow(self, name: str, rowId: int) -> None:
        table = self.tables[name]
        del table[rowId]        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables[name]
        return table[rowId][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)

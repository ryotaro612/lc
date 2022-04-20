class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return str(s)
        rows = [list() for _ in range(numRows)]        
        index_iter = cycle(list(range(numRows))[:-1] + list(reversed(list(range(numRows))))[:-1])        
        for c in s:
            index = next(index_iter)
            rows[index].append(c)
        result = []
        for row in rows:
            result.extend(row)
        return ''.join(result)    

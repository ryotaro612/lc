# [[1,2,3],[0,0,4],[7,6,5]]
# [[0],[0],[6014]]
class Solution:
    inf = 1000000
    def cutOffTree(self, forest: List[List[int]]) -> int:
        n_row = len(forest)
        n_col = len(forest[0])
        trees = []
        for row in range(n_row):
            for col in range(n_col):
                if 1 < forest[row][col]:
                    trees.append((forest[row][col], (row, col)))
        
        trees.sort(key=lambda item: item[0])
        
        res = 0
        from_row = 0
        from_col = 0
        
        for _, (row, col) in trees:
            res += self.computeDist(from_row, from_col, row, col, forest)
            from_row = row
            from_col = col
            if self.inf <= res:
                return -1
        return res
                    
    def encode(self, row, column, n_col):
        return row * n_col + column
    
    def decode(self, i, n_col):
        return i // n_col, i % n_col
    
    def computeDist(self, from_row, from_col, to_row, to_col, forest) -> int:
        n_row = len(forest)
        n_col = len(forest[0])
        d = [[self.inf for _ in range(n_col)] for _ in range(n_row)]
        d[from_row][from_col] = 0
        # print(d)
        que = deque()
        que.append((0, from_row, from_col))
 
        while 0 < len(que):
            dist, row, col = que.popleft()
            if d[row][col] < dist:
                continue
            if row == to_row and col == to_col:
                return d[row][col]
            
            neighbors = []
            if 0 < row:
                neighbors.append((row-1, col))
            if col < n_col - 1:
                neighbors.append((row, col+1))
            if row < n_row - 1:
                neighbors.append((row+1, col))
            if 0 < col:
                neighbors.append((row, col -1))
            
            for next_row, next_col in neighbors:
                if 0 < forest[next_row][next_col] and dist + 1 < d[next_row][next_col]:
                    d[next_row][next_col] = dist + 1
                    que.append((dist+1, next_row, next_col))
        # print(from_row, from_col, to_row, to_col, '->', d[to_row][to_col])
        return d[to_row][to_col]

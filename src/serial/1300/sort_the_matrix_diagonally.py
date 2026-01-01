class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows = len(mat)
        n_cols = len(mat[0])
        for c in range(n_cols):
            ary = self.find(0, c, mat)
            self.assign(mat, ary, 0, c)
    
        for r in range(n_rows):
            ary = self.find(r, 0, mat)
            self.assign(mat, ary, r, 0)
        
        return mat
    
    def find(self, r, c, mat):
        n_rows = len(mat)
        n_cols = len(mat[0])
        ary = []
        while 0 <= r < n_rows and 0 <= c < n_cols:
            ary.append(mat[r][c])
            r += 1
            c += 1
        return sorted(ary)
    
    def assign(self, mat, ary, r, c):
        n_rows = len(mat)
        n_cols = len(mat[0])
        ary = ary[::-1]
        while ary:
            mat[r][c] = ary.pop()
            r += 1
            c += 1

            

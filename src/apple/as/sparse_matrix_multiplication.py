class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        # mat1 * mat2 size is (m, n)
        result = [[0 for _ in range(n)] for _ in range(m)]
        dense_sets = [set() for _ in range(n)]
        for i in range(n):
            for j in range(k):
                if mat2[j][i] != 0:
                    dense_sets[i].add(j)
        
        for i in range(m):
            dense_row = set()
            for j in range(k):
                if mat1[i][j] != 0:
                    dense_row.add(j)
                    
            for j in range(n):
                v = 0
                for l in (dense_row & dense_sets[j]):
                    v += mat1[i][l] * mat2[l][j]
                result[i][j] = v
        return result

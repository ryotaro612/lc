class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n_rows = len(img)
        n_cols = len(img[0])
        result = [[0] * n_cols for _ in range(n_rows)]

        for r in range(n_rows):
            for c in range(n_cols):
                count = 0
                for n_r in [r-1, r, r+1]:
                    for n_c in [c-1, c, c+1]:
                        if 0<=n_r<n_rows and 0<=n_c < n_cols:
                            count += 1
                            result[r][c] += img[n_r][n_c]
                result[r][c] //= count

        return result

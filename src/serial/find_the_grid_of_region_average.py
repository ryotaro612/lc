class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        n_rows = len(image)
        n_cols = len(image[0])

        avg = [[list() for _ in range(n_cols)] for _ in range(n_rows)]
        for r in range(1, n_rows - 1):
            for c in range(1, n_cols - 1):
                region = [[] for _ in range(3)]
                region[0] = image[r-1][c-1:c+2]
                region[1] = image[r][c-1:c+2]
                region[2] = image[r+1][c-1:c+2]

                a = self.is_ok(region, threshold)
                if a >= 0:
                    for s_r in range(r-1, r+2):
                        for s_c in range(c-1, c+2):
                            avg[s_r][s_c].append(a)

        res = [[0] * n_cols for _ in range(n_rows)]
        for r in range(n_rows):
            for c in range(n_cols):
                if len(avg[r][c]):
                    res[r][c] = sum(avg[r][c]) // len(avg[r][c])
                else:
                    res[r][c] = image[r][c]
        return res

    def is_ok(self, region, threshold):
        total = 0
        for r in range(3):
            for c in range(3):
                for s_r, s_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                    if 0 <= s_r < 3 and 0 <= s_c < 3:
                        if abs(region[r][c] - region[s_r][s_c]) > threshold:
                            return -1
                total += region[r][c]
        return total // 9

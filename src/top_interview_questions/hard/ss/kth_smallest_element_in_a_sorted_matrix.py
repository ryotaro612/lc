import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lb, ub = -1000000001, 1000000001
        a = 0
        while ub - lb > 1:
            mid = (ub + lb) // 2
            count = 0
            
            
            row, col = n-1, 0
            while 0 <= row and col <= n-1:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            # print(mid, row, col, count)
            """
            a += 1
            if 5 <= a:
                break
            """
            if k <= count:
                ub = mid
            else:
                lb = mid
        return ub

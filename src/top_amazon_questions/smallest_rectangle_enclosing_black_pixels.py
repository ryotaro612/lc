from collections import deque

class Solution:
    
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n_row = len(image)
        n_col = len(image[0])
                
        
        ub = x + 1
        lb = -1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            for i in range(n_col):
                if image[mid][i] == '1':
                    ub = mid
                    break
            else:
                lb = mid
        top = ub
        
        lb = x - 1
        ub = n_row
        while ub - lb > 1:
            mid = (ub + lb) // 2
            for i in range(n_col):
                if image[mid][i] == '1':
                    lb = mid
                    break
            else:
                ub = mid
        bottom = lb
        
        lb = -1
        ub = y + 1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            
            for i in range(n_row):
                if image[i][mid] == '1':
                    ub = mid
                    break
            else:
                lb = mid
        left = ub
        
        lb = y - 1
        ub = n_col
        while ub - lb > 1:
            mid = (ub + lb) // 2
            for i in range(n_row):
                if image[i][mid] == '1':
                    lb = mid
                    break
            else:
                ub = mid
        right = lb
        
        return (bottom - top + 1) * (right - left + 1)

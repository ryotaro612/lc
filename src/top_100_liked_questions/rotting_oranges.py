import heapq

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        n_row = len(grid)
        n_col = len(grid[0])
        
        heap = []
        
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    heapq.heappush(heap, (0, r, c))
        
        result = 0
        
        while heap and num_fresh:
            mini, r, c = heapq.heappop(heap)
            
            for next_r, next_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= next_r < n_row and 0 <= next_c < n_col:
                    if grid[next_r][next_c] == 1:
                        num_fresh -= 1
                        grid[next_r][next_c] = 2
                        heapq.heappush(heap, (mini+1, next_r, next_c))
            
            result = max(result, mini+1)
        
        if num_fresh:
            return -1
        else:
            return result

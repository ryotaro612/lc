import heapq

class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        
        n = len(coins)
        
        d = [float('inf')] * n
        
        d[0] = 0
        heap = [[d[0], 0]]
        
        while heap:
            
            dist, node = heapq.heappop(heap)
            
            if d[node] < dist:
                continue
                
            neighbors = [i for i in range(node + 1, min(node + maxJump + 1, n)) if coins[i] != -1]
            
            for neighbor in neighbors:
                new_dist = d[node] + coins[neighbor]
                
                if new_dist < d[neighbor]:
                    d[neighbor] = new_dist
                    
                    heapq.heappush(heap, [d[neighbor], neighbor])
                    
    
        result = []
        self.find_path(d, 0, result, coins, maxJump)
        return [i + 1 for i in result]
    
    def find_path(self, d, i, result, coins, maxJump):
        n = len(coins)
        
        result.append(i)
        
        if i == n - 1:
            return True
        
        for j in range(i + 1, min(n, i + maxJump + 1)):
            if d[i] + coins[j] == d[j]:
                if self.find_path(d, j, result, coins, maxJump):
                    return True
        
        result.pop()
        return False

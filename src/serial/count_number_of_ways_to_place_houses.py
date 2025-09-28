class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        prev = [1, 0, 0, 0]
        0 -> 0   0, 1, 2, 3
             0   

        1 -> 1   0, 2
             0
        2 -> 0   0, 1
             1
        3 -> 1   0
             1
        cur =  
        """
        mod = 10**9 + 7
        prev = [0] * 4
        prev[0] = 1
        cur = [0] * 4
        for _ in range(n):
            cur[0] += sum(prev) % mod
            cur[1] = (prev[0] + prev[2]) % mod
            cur[2] = (prev[0] + prev[1]) % mod
            cur[3] = prev[0]
            prev = cur
            cur = [0] * 4
        
        return sum(prev) % mod            

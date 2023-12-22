class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * 2001 for _ in range(n)]
        dp[0][1] = True

        stone_index = dict()
        for i, stone in enumerate(stones):
            stone_index[stone] = i
        
        for i in range(n-1):
            for step in range(1, 2001):
                if dp[i][step]:
                    next_position = stones[i] + step
                    if next_position in stone_index:
                        for next_step in [step-1, step, step+1]:
                            if 1 <=next_step <=2000:
                                dp[stone_index[next_position]][next_step] = True
        
        for v in dp[n-1]:
            if v:
                return True
        return False
                            
                    


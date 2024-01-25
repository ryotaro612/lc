class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        pattern = [0, 0, 0, 0]
        if sum(matchsticks) % 4:
            return False
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        
        return self.rec(pattern, 0, target, matchsticks)
    
    def rec(self, pattern, i, target, matchsticks):
        if i == len(matchsticks):
            return len(set(pattern)) == 1
        for pos in range(4):
            pattern[pos] += matchsticks[i]
            if pattern[pos] <= target and self.rec(pattern, i+1, target, matchsticks):
                return True
            pattern[pos] -= matchsticks[i]
        return False

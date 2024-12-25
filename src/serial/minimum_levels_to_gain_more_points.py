class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        scores = [0] * n
        for i in range(n-1, -1, -1):
            if possible[i]:
                score = 1
            else:
                score = -1
            if i == n-1:
                scores[i] = score
            else:
                scores[i] = score + scores[i+1]
        
        alice = 0
        for i in range(n):
            if possible[i]:
                alice += 1
            else:
                alice -= 1
            
            if i < n-1:
                if alice > scores[i+1]:
                    return i+1
        return -1

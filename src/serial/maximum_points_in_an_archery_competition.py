class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bob_max = 0
        
        for mask in range(1<<11):
            pattern = []
            arrows = numArrows
            score = 0
            for i in range(11):
                if mask & (1<<i):
                    if aliceArrows[i] < arrows:
                        pattern.append(aliceArrows[i] + 1)
                        arrows -= aliceArrows[i] + 1
                        score += i
                    else:
                        pattern.append(0)
                else:
                    pattern.append(0)

            pattern.append(arrows)    
            if aliceArrows[-1] < pattern[-1]:
                score += 11
            
            if bob_max < score:
                result = pattern
                bob_max = score
        
        return result


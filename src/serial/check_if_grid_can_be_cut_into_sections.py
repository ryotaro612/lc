class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        vertical = sorted([[rec[1], rec[3]] for rec in rectangles])
        horizontal = sorted([[rec[0], rec[2]] for rec in rectangles])

        return self.check(vertical) or self.check(horizontal)
    
    def check(self, lines):
        count = 0
        n = len(lines)
        threshold = 0
        for i in range(n - 1):
            threshold = max(threshold, lines[i][1])
            if threshold <= lines[i+1][0]:
                count += 1
        
        return count >= 2

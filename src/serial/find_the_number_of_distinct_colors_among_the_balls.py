from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = dict()
        color_freq = defaultdict(int)
        result = []
        for ball, color in queries:
            if ball in ball_color:
                c = ball_color[ball]
                color_freq[c] -= 1
                if color_freq[c] == 0:
                    del color_freq[c]
            
            ball_color[ball] = color
            color_freq[color] += 1
            result.append(len(color_freq))
        
        return result

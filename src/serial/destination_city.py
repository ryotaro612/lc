class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        directions = dict()
        for [start, end] in paths:
            directions[start] = end
        
        pos =paths[0][0]
        while pos in directions:
            pos = directions[pos]
        
        return pos

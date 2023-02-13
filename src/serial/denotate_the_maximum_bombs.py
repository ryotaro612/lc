"""
[[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]]
[[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g =[[] for _ in range(n)]

        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = (x1 - x2) ** 2 + (y1-y2) ** 2 
                if dist <= r1 ** 2:
                    g[i].append(j)
                if dist <= r2 ** 2:
                    g[j].append(i)
            
        result = 0
        for i in range(n):
            reachable = set()
            self.find(i, g, reachable)
            result = max(result, len(reachable))
        return result

    def find(self, node, g, reachable):
        if node in reachable:
            return
        reachable.add(node)
        for neighbor in g[node]:
            self.find(neighbor, g, reachable)

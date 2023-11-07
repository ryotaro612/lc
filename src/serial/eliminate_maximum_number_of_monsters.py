class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        monsters = sorted([[d/s, d, s] for d, s in zip(dist, speed)])
        weapon = 0
        for i, [time, d, s] in enumerate(monsters):
            if weapon * s >= d:
                return i
            weapon += 1
        return len(dist)

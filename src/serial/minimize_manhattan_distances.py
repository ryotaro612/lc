class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        us = sorted([(x+y, i) for i, [x, y] in enumerate(points)])
        vs = sorted([(x-y, i) for i, [x, y] in enumerate(points)])
        remove_cands = {
            us[0][1], us[-1][1], vs[0][1], vs[-1][1]
        }

        result = min([
            self.calc_min_distance([p for i, p in enumerate(points) if i != remove_i])
            for remove_i
            in remove_cands
        ])
        return result
        
    def calc_min_distance(self, points):
        us = sorted([x+y for x, y in points])
        vs = sorted([x-y for x, y in points])
        return max(us[-1] - us[0], vs[-1] - vs[0])

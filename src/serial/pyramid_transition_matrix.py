from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        allowed_map = defaultdict(list)

        for [l, r, t] in allowed:
            allowed_map[(l, r)].append(t)
        
        cache = dict()
        return self.rec(bottom, allowed_map, cache)

    def rec(self, bottom, allowed_map, cache):
        if len(bottom) == 1:
            return True
        
        if bottom in cache:
            return cache[bottom]
        
        rows = []
        self.build_row([], bottom, allowed_map, rows)
        # print(bottom, rows)
        for row in rows:
            if self.rec(row, allowed_map, cache):
                return True
        
        return False

    def build_row(self, building, bottom, allowed_map, rows):
        if len(building) == len(bottom) - 1:
            rows.append(''.join(building))
            return
        
        n = len(building)
        if n == 0:
            for c in allowed_map[(bottom[0], bottom[1])]:
                building.append(c)
                self.build_row(building, bottom, allowed_map, rows)
                building.pop()
        else:
            for c in allowed_map[(bottom[len(building)], bottom[len(building)+1])]:
                building.append(c)
                self.build_row(building, bottom, allowed_map, rows)
                building.pop()
        

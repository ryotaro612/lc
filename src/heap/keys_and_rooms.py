"""
[[1],[2],[3],[]]
[[1,3],[3,0,1],[2],[0]]
"""
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        par = [-1] * n
        que = deque([0])
        while que:
            room = que.pop()
            for key in rooms[room]:
                if not self.is_same(key, room, par):
                    que.append(key)
                self.unite(room, key, par)
        
        return -par[self.find_root(0, par)] == n
    
    def find_root(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.find_root(par[i], par)
        return par[i]
    
    def is_same(self, a, b, par):
        return self.find_root(a, par) == self.find_root(b, par)
    
    def unite(self, a, b, par):
        if self.is_same(a, b, par):
            return
        root_a = self.find_root(a, par)
        root_b = self.find_root(b, par)
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b

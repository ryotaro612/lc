"""
table
MUC -> [('LHR', 1)]
JFK => [('MUC', 1)]

result => [JFK, MUC]

JFK -> MUC
MUC -> JFK
JFK -> MUC
MUC -> JFK
JFK -> MUC
MUC -> JFK
JFK -> MUC
MUC -> JFK
O(N/2log(N/2))

[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightmap = dict()
        for ticket in tickets:
            [start, to] = ticket
            flightmap.setdefault(start, [])
            flightmap[start].append(to)
        for start in flightmap:
            flightmap[start].sort(reverse=True)
            
        result = []
        self.dfs(flightmap, 'JFK', result)
        return result[::-1]

    def dfs(self, flightmap, origin, result):
        if origin not in flightmap:
            result.append(origin)
            return
        dests =flightmap[origin]

        while dests:
            dest = dests.pop()
            self.dfs(flightmap, dest, result)
        
        result.append(origin)

"""
[["oxlp","rxekw"],["wusp","py"],["jiljl","ocki"],["wna","ahd"],["btzo","oxlp"],["tf","gdzjl"],["btzo","xfzuo"],["jiljl","gdzjl"],["hpic","wusp"],["z","qs"],["tkgna","wna"],["wusp","btzo"],["ocki","z"],["ttfkc","py"],["xfzuo","xfzuo"],["ahd","xfzuo"],["ocki","py"],["jnsz","py"],["wna","wna"],["wusp","wusp"],["ttfkc","py"],["qs","dci"],["wusp","wusp"],["btzo","oxlp"],["tf","tf"],["ocki","ocki"],["z","qs"],["qs","dci"],["z","qs"],["btzo","btzo"]]

[8.32,9.23,2.96,8.64,8.66,1.55,1.5,4.12,7.2,9.26,5.62,8.07,9.75,2.03,1,1.08,3.96,8.41,1,1,1.35,6.59,1,7.47,1,1,9.26,6.59,9.26,1]
"""
from collections import defaultdict

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        g = defaultdict(lambda: dict())
        for [node1, node2], v in zip(equations, values):
            g[node1][node2] = 1 / v # node2 = node1 * g[node1][node2]
            g[node2][node1] = v
         
        vals = dict()
        for node1, node2 in equations:
            if node1 in vals:
                continue
            vals[node1] = 1
            if self.hasContradiction(node1, g, vals):
                return True
        for [a, b], v in zip(equations, values):
            if abs(vals[a] / vals[b] - v) > 0.00001:
                return True
        return False

    def hasContradiction(self, node, g, vals):
        
        neighbors = list(g[node].keys())
        for neighbor in neighbors:
            v = g[node][neighbor] * vals[node]
            if neighbor in vals:
                if abs(vals[neighbor] - v) > 0.00001:
                    return True
                else:
                    continue
            else:
                vals[neighbor] = v
                # del g[node][neighbor]
                # del g[neighbor][node]
                if self.hasContradiction(neighbor, g, vals):
                    return True
        return False

class Solution:

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        paths = [[] for _ in range(len(roads) + 1)]
        for node1, node2 in roads:
            paths[node1].append(node2)
            paths[node2].append(node1)
        result = 0
        for child in paths[0]:
            result += self.rec(child, 0, paths, seats)[1]
        return result 
        
    def rec(self, node, parent, paths, seats):
        if node is None:
            return 0, 0
        
        fuels = 0
        nodes = 1
        for child in paths[node]:
            if child == parent:
                continue
            
            c_nodes, c_fuels = self.rec(child, node, paths, seats)
            nodes += c_nodes
            fuels += c_fuels
        
        fuels += nodes // seats
        if nodes % seats:
            fuels += 1
        
        return nodes, fuels
            

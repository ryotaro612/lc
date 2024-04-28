class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        n_nodes = [0] * n
        weights = [0] * n
    
        self.count_weights(0, -1, g, n_nodes, weights)

        result = [0] * n
        result[0] = weights[0]
        for child in g[0]:
            if child != 0:
                self.accumulate(child, 0, g, n_nodes, weights, result)

        return result


    def count_weights(self, node, parent, g, n_nodes, weights):
        n_nodes[node] = 1
        weights[node] = 0
        
        for child in g[node]:
            if child == parent:
                continue
            self.count_weights(child, node, g, n_nodes, weights)
            n_nodes[node] += n_nodes[child]
            weights[node] += weights[child] + n_nodes[child]
    
    def accumulate(self, node, parent, g, n_nodes, weights, result):
        result[node] = result[parent] - n_nodes[node] + len(g) - n_nodes[node]
        for child in g[node]:
            if parent != child:
                self.accumulate(child, node, g, n_nodes, weights, result)

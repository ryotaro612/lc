import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[] for _ in range(n)]
        for f, t, c in edges:
            self.g[f].append([t, c])
            

    def addEdge(self, edge: List[int]) -> None:
        self.g[edge[0]].append(edge[1:])

    def shortestPath(self, node1: int, node2: int) -> int:
        d = [float('inf')] * len(self.g)
        d[node1] = 0
        heap = [[0, node1]]
        while heap:
            cost, node = heapq.heappop(heap)
            if d[node] < cost:
                continue
            
            for neighbor, next_c in self.g[node]:
                new_cost = next_c + d[node]
                if new_cost < d[neighbor]:
                    d[neighbor] = new_cost
                    heapq.heappush(heap, [d[neighbor], neighbor])

        return d[node2] if d[node2] < float('inf') else -1 
                


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

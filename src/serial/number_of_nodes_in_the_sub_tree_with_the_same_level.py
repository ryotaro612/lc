from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = [[] for _ in range(n)]

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        ans = [0] * n
        counter = defaultdict(int)
        self.traverse(0, -1, g, labels, ans, counter)
    
        return ans
    

    def traverse(self, node, parent, g, labels, ans, counter):
        counter[labels[node]] += 1

        for child in g[node]:
            if child == parent:
                continue
            child_counter = defaultdict(int)
            
            self.traverse(child, node, g, labels, ans, child_counter)
            
            for c, freq in child_counter.items():
                counter[c] += freq
        

        ans[node] = counter[labels[node]]

"""
"""
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = [float('inf')] * n
        v_to_i = defaultdict(list)
        for i, num in enumerate(arr):
            v_to_i[num].append(i)
        d[0] = 0
        que = deque([0])
        while que:
            node = que.popleft()
            cost = d[node] + 1
            
            for neighbor in [neighbor for neighbor in v_to_i[arr[node]] + [node - 1, node + 1] if 0 <= neighbor < n]:

                if d[neighbor] > cost:
                    d[neighbor] = cost
                    que.append(neighbor)
            v_to_i[arr[node]]=[]
        # print(d)
        return d[n-1]
            

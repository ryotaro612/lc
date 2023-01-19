
from collections import deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        from_to = [set() for _ in range(n)]
        to_from = [set() for _ in range(n)]
        
        for relation in relations:
            from_to[relation[0]-1].add(relation[1]-1)
            to_from[relation[1]-1].add(relation[0]-1)
        
        que = deque()
        for node in range(n):
            if not to_from[node]:
                que.append(node)
                
        num_semesters = 0
        while que:
            next_que = deque()
            while que:
                to = que.popleft()
                for neighbor in from_to[to]:
                    to_from[neighbor].remove(to)
                    if not to_from[neighbor]:
                        next_que.append(neighbor)
            que = next_que
            num_semesters += 1
        
        for from_set in to_from:
            if from_set:
                return -1
            
        return num_semesters

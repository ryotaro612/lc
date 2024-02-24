from collections import defaultdict, deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        has_secret = [False] * n
        has_secret[firstPerson] = has_secret[0] = True

        time_people = defaultdict(lambda: defaultdict(list))
        for a, b, time in meetings:
            time_people[time][a].append(b)
            time_people[time][b].append(a)
        for g in [time_people[time] for time in sorted(list(time_people.keys()))]:
            people = list(g.keys())
            que = deque([p for p in people if has_secret[p]])
            if len(que) == len(people):
                continue
            while que:
                person = que.popleft() 
                for neighbor in [neighbor for neighbor in g[person] if not has_secret[neighbor]]:
                    has_secret[neighbor] = True
                    que.append(neighbor)
        
        return [i for i, v in enumerate(has_secret) if v]

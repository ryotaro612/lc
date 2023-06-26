from collections import defaultdict


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for i, parent in enumerate(ppid):
            graph[parent].append(pid[i])

        return self.find_kill(graph, kill)

    def find_kill(self, graph, kill):
        result = [kill]
        for child in graph[kill]:
            result.extend(self.find_kill(graph, child))
        return result

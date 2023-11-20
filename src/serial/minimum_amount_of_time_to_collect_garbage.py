class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        result = 0
        n = len(garbage)
        for garbage_type in 'GPM':
            move_cost = 0
            for i in range(n):
                for c in garbage[i]:
                    if c == garbage_type:
                        result += 1
                        result += move_cost
                        move_cost = 0
                if i < n-1:
                    move_cost += travel[i]
        return result

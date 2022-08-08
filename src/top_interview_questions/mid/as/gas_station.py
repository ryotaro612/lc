
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        gas = gas + gas
        cost = cost + cost
        
        start, end = 0, 0
        tank = 0
        for start in range(n):
            end = max(end, start)
            
            while end - start < n and cost[end] <= tank + gas[end]:
                tank += gas[end] - cost[end]
                end += 1
            
            if end - start == n:
                return start
            
            if start < end:
                tank += cost[start] - gas[start]
        
        return -1


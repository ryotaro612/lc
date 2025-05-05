class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        costs = [float('inf')] * n
        types = [i for i in range(n)]
        result = float('inf')
        for r in range(n):
            for i in range(n):
                costs[types[i]] = min(costs[types[i]], nums[i])

            result = min(result, r * x + sum(costs))
            
            next_types = [0] * n
            for i in range(n):
                next_types[i] = types[(i+1)%n]
            types = next_types

        
        return result
    

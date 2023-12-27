class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        left = 0
        n = len(colors)
        for right in range(n):
            if right == n - 1 or colors[right+1] != colors[left]:
                total_cost = 0
                max_cost = 0
                for i in range(left, right+1):
                    total_cost += neededTime[i]
                    max_cost = max(max_cost, neededTime[i])
                result += total_cost - max_cost
                left = right+1
        return result

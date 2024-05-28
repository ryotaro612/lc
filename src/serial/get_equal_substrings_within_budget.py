    class Solution:
        def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
            result = 0
            right = 0
            n = len(s)
            cost = 0
            for left in range(n):
                right = max(right, left)
                while right < n and cost + self.calc_cost(s, t, right) <= maxCost:
                    cost += self.calc_cost(s, t, right)
                    right += 1
                
                result = max(result, right - left)
                if left < right:
                    cost -= self.calc_cost(s, t, left)

            return result
        
        def calc_cost(self, s, t, pos):
            return abs(ord(s[pos]) - ord(t[pos]))

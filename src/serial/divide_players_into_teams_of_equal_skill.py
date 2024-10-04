class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        pairs = []
        left = 0
        right = len(skill)-1

        sum_patterns = set()
        result = 0
        while left < right:
            result += skill[left] * skill[right]
            sum_patterns.add(skill[left] + skill[right])
            left += 1
            right -= 1
        
        if len(sum_patterns) == 1:
            return result
        else:
            return -1

        
        

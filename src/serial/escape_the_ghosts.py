class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])

        for r, c in ghosts:
            
            if dist >= abs(target[0] - r) + abs(target[1] - c):
                return False
        return True

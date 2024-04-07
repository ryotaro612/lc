class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        """
        accept_range = [0, 0]
        for c in s:
            if c == '(':
                accept_range[0] += 1
                accept_range[1] += 1
            elif c == ')':
                accept_range[0] -= 1
                accept_range[1] -= 1
            else:
                accept_range[0] -= 1
                accept_range[1] += 1
            
            if accept_range[1] < 0:
                return False
            accept_range[0] = max(0, accept_range[0])
        
        return accept_range[0] <= 0 <= accept_range[1]

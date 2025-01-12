class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        left = []
        unlock = []

        if len(s) % 2:
            return False

        for i in range(len(s)):
            if locked[i] == '0':
                unlock.append(i)
                continue
            if s[i] == '(':
                left.append(i)
            else:
                if left:
                    left.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False
        
        while left and unlock and left[-1] < unlock[-1]:
            left.pop()
            unlock.pop()

        return left == [] 

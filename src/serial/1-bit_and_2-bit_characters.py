class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        stack = bits[::-1]

        while len(stack) > 1:
            if stack[-1] == 0:
                stack.pop()
            else:
                stack.pop()
                stack.pop()
        
        return len(stack) == 1

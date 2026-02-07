class Solution:
    def addMinimum(self, word: str) -> int:
        """
        prev = 'a' or 'b' 'c'
        result = 0
        for c in word:

        """
        result = 0
        prev = word[0]
        if prev == 'b':
            result += 1
        elif prev == 'c':
            result += 2
        
        for c in word[1:]:
            if c == 'a':
                if prev == 'a':
                    result += 2
                elif prev == 'b':
                    result += 1
            elif c == 'b':
                if prev == 'b':
                    result += 2
                elif prev == 'c':
                    result += 1
            else: # c == 'c'
                if prev == 'a':
                    result += 1
                elif prev == 'c':
                    result += 2
            prev = c
        
        if prev == 'a':
            result += 2
        elif prev == 'b':
            result += 1
        
        return result

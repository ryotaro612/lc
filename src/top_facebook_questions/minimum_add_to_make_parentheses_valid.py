class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = 0
        result = 0
        
        for c in s:
            if c == '(':
                counter += 1
            else:
                if counter > 0:
                    counter -= 1
                else:
                    result += 1
        
        return result + counter

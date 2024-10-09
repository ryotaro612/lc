class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        counter = 0
        for c in s:
            if c == '(':
                counter += 1
            else:
                if counter == 0:
                    result += 1
                else:
                    counter -= 1
        
        return result + counter


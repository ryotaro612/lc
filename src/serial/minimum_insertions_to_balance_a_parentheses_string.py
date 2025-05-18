class Solution:
    def minInsertions(self, s: str) -> int:
        counter = 0
        result = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                counter += 1
                i += 1
                continue
            
            # ))
            if i < n - 1 and s[i+1] == ')':
                if counter:
                    counter -= 1
                    i += 2
                    continue
                else:
                    result += 1 # (
                    i += 2
                    continue
            else:
                if counter:
                    result += 1 # )
                    counter -= 1
                    i += 1
                    continue
                else:
                    result += 2 # ( )
                    i += 1
                    continue
        
        return result + counter * 2

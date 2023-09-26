"""
"abacb"
"""
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        result = []
        st = set()
        for c in s:
            while result and c not in st and c < result[-1] and counter[result[-1]]:
                st.remove(result.pop())

            if c not in st:
                result.append(c)
                st.add(c)    
                    
            counter[c] -= 1
        return ''.join(result)

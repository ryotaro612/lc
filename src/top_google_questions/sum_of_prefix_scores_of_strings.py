"""
a,1 -> b,1 -> c,1

a,2 -> b,2 -> c,1

a,2 -> b,2 -> c,1
b,1 -> c,1

a,2 -> b,2 -> c,1
b,2 -> c,1

["abc","ab","bc","b"]
 ["abcd"]
"""
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = [0, dict()]
        
        for word in words:
            node = root
            for c in word:
                if c in node[1]:
                    node = node[1][c]
                    node[0] += 1
                else:
                    node[1][c] = [1, dict()]
                    node = node[1][c]
        
        result = []
        
        for word in words:
            
            count = 0
            node = root
            for c in word:
                node = node[1][c]
                count += node[0]
            
            result.append(count)
        
        return result

"""
["abc","bde","cefg"]
"""
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n_row = len(words)
        n_col = len(words[0])
        if n_row != n_col:
            return False
            
        for i in range(n_row):
            for j in range(i, n_row):
                if i < len(words[j]):
                    if j < len(words[i]):
                        if words[j][i] != words[i][j]:
                            return False
                    else:
                        return False
                else:
                    if j < len(words[i]):
                        return False
                    
        max_col = max([len(word) for word in words])
        
        return max_col == n_row
            

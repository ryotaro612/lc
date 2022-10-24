class Solution:
    def appealSum(self, s: str) -> int:
        positions = [[-1] for _ in range(26)]
        
        for i, c in enumerate(s):
            indice = ord(c) - ord('a')
            positions[indice].append(i)
        
        n = len(s)
        result = 0
        for i in range(26):
            positions[i].append(n)
            
            n_unexist = n * (n-1) // 2 + n
            for j in range(0, len(positions[i])-1):
                size = positions[i][j+1] - positions[i][j] - 1
                n_unexist -= size * (size-1) // 2 + size
            # print(i, positions[i], n_unexist)
            result += n_unexist
        
        return result

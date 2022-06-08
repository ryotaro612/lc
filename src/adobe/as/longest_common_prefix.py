class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        
        length = min([len(s) for s in strs])
        
        for i in range(length):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return ''.join(result)
            result.append(c)
        return ''.join(result)

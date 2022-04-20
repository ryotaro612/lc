class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        for string in strs:
            min_length = min(min_length, len(string))
            
        for index in range(min_length):
            c = strs[0][index]
            for str_index in range(1, len(strs)):
                if c != strs[str_index][index]:
                    return strs[0][:index]
        return strs[0][:min_length]

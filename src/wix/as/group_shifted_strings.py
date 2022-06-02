class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group_dict = dict()
        
        for string in strings:
            shift = 26 - ord(string[0]) - ord('a')
            letters = []
            for c in string:
                letters.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
            
            normalized = ''.join(letters)
            group_dict.setdefault(normalized, [])
            group_dict[normalized].append(string)
        
        return list(group_dict.values())

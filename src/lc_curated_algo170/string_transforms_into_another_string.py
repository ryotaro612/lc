class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        conv = dict()
        n = len(str1)
        
        for c1, c2 in zip(str1, str2):
            if c1 in conv:
                if conv[c1] != c2:
                    return False
            else:
                conv[c1] = c2
                
        if len(set(str2)) == 26:
            return False
        return True


    

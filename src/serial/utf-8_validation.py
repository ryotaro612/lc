class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            if data[i] >> 7 == 0:
                i+= 1
            elif i < n - 1 and (data[i] >> 5) == 6: # 110...
                if data[i+1] >> 6    == 2:
                    i+=2
                else:
                    return False
            elif i < n-2 and data[i] >> 4 == 8+4+2:
                if (data[i+1] >> 6) == (data[i+2] >>6) == 2:
                    i+=3
                else:
                    return False
            elif i < n-3 and data[i] >> 3 == 16+8+4+2:
                if (data[i+1] >> 6) == (data[i+2] >> 6) == (data[i+3] >> 6) == 2:
                    i+=4
                else:
                    return False
            else:
                return False
        return True
    
   

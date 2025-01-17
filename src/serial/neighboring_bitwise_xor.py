class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
         
        n = len(derived)
        for i in range(32):
            ok = False
            for assume in range(1):
                current = assume
                for j in range(n):
                    derived_bit = 1 & (derived[j] >> i)
                    if derived_bit:
                        if current:
                            current = 0
                        else:
                            current = 1
                    else:
                        if current:
                            current = 1
                        else:
                            current = 0
                if assume == current:
                    ok = True
            if not ok:
                return False
        
        return True

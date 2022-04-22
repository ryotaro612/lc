class Solution:
    def isHappy(self, n: int) -> bool:
        used =set()
        
        current = ''.join(sorted(str(n)))
        
        while current not in used:
            if current == "1":
                return True
            used.add(current)
            next_val = 0
            for c in current:
                next_val += int(c) * int(c)

            current =''.join(sorted(str(next_val))) 
        return False

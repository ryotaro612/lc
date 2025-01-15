class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = 0
        while num2:
            if num2 & 1:
                count += 1
            num2 >>= 1
        
        temp = num1
        set_pos = []
        i = 0
        while temp:
            if temp & 1:
                set_pos.append(i)
            temp >>= 1
            i += 1

        if len(set_pos) <= count:
            result = 0
            for i in set_pos:
                result |= 1 << i
            set_pos = set(set_pos)
            i = 0
            while len(set_pos) < count:
                if i not in set_pos:
                    result |= 1 << i
                    count -= 1
                i += 1
                
            return result
        
        result = 0
        for i in range(count):
            result |= 1 << set_pos[-1 - i]
        
        return result

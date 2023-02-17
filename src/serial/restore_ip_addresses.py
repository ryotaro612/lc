class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        self.build(0, [], result, [int(c) for c in s])
    
        return result

    
    def build(self, i, current, result, digits):
        n = len(digits)
        if i == n:
            if len(current) == 4:
                result.append('.'.join([str(part) for part in current]))
            return
        
        d = int(digits[i])
        if i and 0 <= current[-1] * 10 + d <= 255 and current[-1] != 0:
            current[-1] = current[-1] * 10 + d
            self.build(i+1, current, result, digits)
            current[-1] //= 10
        if len(current) < 4:
            current.append(d)
            self.build(i+1, current, result, digits)
            current.pop()

        

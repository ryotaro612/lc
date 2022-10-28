class Solution:
    def toHex(self, num: int) -> str:
        result = []
        for _ in range(8):
            x = num & 15
            result.append(self.to_hex(x))
            num >>= 4
            if num == 0:
                break
        return ''.join(reversed(result))
    
    def to_hex(self, x):
        if x < 10:
            return str(x)
        else:
            return chr(ord('a') + x - 10)

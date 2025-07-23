class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        return max(self.calc(list(s), x, ['a', 'b'], y, ['b', 'a']), self.calc(list(s), y, ['b', 'a'], x, ['a', 'b']))

    def calc(self, s, x, x_sub, y, y_sub):
        result = 0

        while True:
            s, x_point = self.remove(s, x_sub, x)
            s, y_point = self.remove(s, y_sub, y)

            result += x_point + y_point
            if x_point + y_point == 0:
                break
        
        return result

    def remove(self, s, sub, x):
        stk = []
        result = 0
        for c in s:
            stk.append(c)
            while len(stk) >= 2 and stk[-2:] == sub:
                result += x
                stk.pop()
                stk.pop()
        
        return stk, result
    

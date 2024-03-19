class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        num1 -> (a, b)
        num2 -> (c, d)
        (a*c-b*d,a*d+b*c)
        """
        a, b = self.parse(num1)
        c, d = self.parse(num2)
        real = a*c-b*d
        img = a*d + b*c

        return str(real) + '+' + str(img) + 'i'

    def parse(self, num: str):
        plus_pos = num.find('+')
        real = int(num[:plus_pos])
        img = int(num[plus_pos+1:len(num)-1])
        return real, img
        

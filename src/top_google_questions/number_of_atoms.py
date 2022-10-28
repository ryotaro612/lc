"""
"()"
""K(A)3Bad""
"""
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        symbol = ''
        num = 0
        freq = dict()
        level = 0
        for c in formula:
            if c.isupper():
                self.consume(symbol, num, level, freq, stack)
                num = 0
                symbol = c
                freq = dict()
                
            elif c.islower():
                symbol += c
            
            elif c.isdigit():
                num *= 10
                num += int(c)
                
            elif c == '(':
                self.consume(symbol, num, level, freq, stack)
                symbol = ''
                num = 0
                level += 1
                freq = dict()
            
            elif c == ')':
                self.consume(symbol, num, level, freq, stack)
                level -= 1
                symbol = ''
                num = 0
                freq = stack.pop()[0]
                
            # print(c, freq, symbol, num, level, stack)
        self.consume(symbol, num, level, freq, stack)
        # print('->', freq, symbol, num, level, stack)
        result = []
        for k in sorted(freq):
            result.append(k)
            if freq[k] > 1:
                result.append(str(freq[k]))
        
        return ''.join(result)
                
                
    def consume(self, symbol, num, level, freq, stack):
        if symbol:
            freq[symbol] = 1
        if num > 0:
            for k in freq:
                freq[k] *= num
        
        while stack and stack[-1][1] == level:
            prev_freq = stack.pop()[0]
            for k in prev_freq:
                freq[k] = prev_freq[k] + freq.get(k, 0)
        stack.append((freq, level))
        
        

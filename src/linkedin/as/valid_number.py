class Solution:
    def isNumber(self, s: str) -> bool:
        delim = None
        if 'e' in s:
            delim = 'e'
        elif 'E' in s:
            delim = 'E'
        if delim is None:
            return self.isDecimal(s) or self.isInt(s)
        else:
            tokens = s.split(delim)
            if len(tokens) == 2:
                return (self.isDecimal(tokens[0]) or self.isInt(tokens[0])) and self.isInt(tokens[1])
            else:
                return False
    
    def isDecimal(self, s):
        n = len(s)
        if n == 0:
            return False
        start = 0
        if s[0] in {'+', '-'}:
            start = 1
        tokens = s[start:].split('.')
        if len(tokens) != 2:
            return False
        left, right = tokens[0], tokens[1]
        # One or more digits, followed by a dot '.'.
        if len(right) == 0:
            return left.isdigit()
        # A dot '.', followed by one or more digits.
        elif len(left) == 0:
            return right.isdigit()       
        #  One or more digits, followed by a dot '.', followed by one or more digits.
        else:
            return left.isdigit() and right.isdigit()
    def isInt(self, s):
        n = len(s)
        if n == 0:
            return False
        start = 0
        if s[0] in {'+', '-'}:
            start = 1
        return s[start:].isdigit()

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.check(s, p)
    
    def check(self, s: str, p: str):
        # print(s, ",", p, s == p)
        if p == "":
            return s == ""
        if s == "":
            if p == "":
                return True
            elif 1 < len(p):
                if p[1] == '*':
                    return self.check(s, p[2:])
                else:
                    return False
            else:
                return False
            
        if 1 == len(p):
            if s[0] == p[0] or p[0] == '.':
                return self.check(s[1:], p[1:])
            else:
                return False
        else:
            if p[1] == '*':
                if s[0] == p[0] or p[0] == '.':
                    return self.check(s[1:], p) or self.check(s, p[2:])
                else:
                    return self.check(s, p[2:])
            elif s[0] == p[0] or p[0] == '.':
                return self.check(s[1:], p[1:])
            else:
                return False
                

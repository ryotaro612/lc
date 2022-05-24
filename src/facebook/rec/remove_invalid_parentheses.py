class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        result = set()
        
        self.build(s, left, right, 0, [], 0,result)
        return list(result)
    
    def build(self, s, left, right, pos, sub, stack, result):
        n = len(s)
        if pos == n:
            if left == 0 and right == 0 and stack == 0:
                result.add(''.join(sub))
            return
        
        delta = 0
        if s[pos] == '(':
            if left > 0:
                self.build(s, left-1, right, pos+1, sub, stack, result)
            delta = 1
        elif s[pos] == ')':
            if right > 0:
                self.build(s, left, right-1, pos+1, sub, stack, result)
            delta = -1
        if stack + delta >= 0:    
            sub.append(s[pos])
            self.build(s, left, right, pos+1, sub, stack + delta, result)
            sub.pop()

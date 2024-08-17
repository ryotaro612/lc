class Solution:
    def evaluate(self, expression: str) -> int:
        a = []
        for c in expression:
            if c in {'(', ')'}:
                a.append(' ')
                a.append(c)
                a.append(' ')
            else:
                a.append(c)
        exprs = [c for c in ''.join(a).split() if c]
        # print(exprs)
        return self.eval(dict(), 0, exprs)[0]
    
    def eval(self, env, pos, exprs):

        if exprs[pos] != '(':
            # print(exprs[pos])
            if exprs[pos].isdigit() or exprs[pos].startswith('-'):
                # print(env, exprs[pos:pos+1], int(exprs[pos]))
                return int(exprs[pos]), pos + 1
            else:
                # print(env, exprs[pos:pos+1], env[exprs[pos]])
                return env[exprs[pos]], pos + 1
            
        if exprs[pos+1] in {'add', 'mult'}:
            e1, pos1 = self.eval(env, pos+2, exprs)
            e2, pos2 = self.eval(env, pos1, exprs)
            if exprs[pos + 1] == 'add':
                return e1 + e2, pos2 + 1
            else:
                return e1 * e2, pos2 + 1

        chunks = [pos+2]
        
        while exprs[chunks[-1]] != ')':
            chunks.append(self.chunk(chunks[-1], exprs))
            
        chunks.pop()
        i = 0
        new_env = {k: env[k] for k in env}
        while i < len(chunks) - 1:
            new_env[exprs[chunks[i]]], _ = self.eval(new_env, chunks[i+1], exprs)
            i += 2
        
        res, _ = self.eval(new_env, chunks[-1], exprs)
        p = self.chunk(pos, exprs)
        # print(new_env, res, exprs[pos:p])
        return res, p

    def chunk(self, pos, exprs):
        if exprs[pos] != '(':
            return pos + 1
        stack = 1
        pos += 1
        while stack:
            if exprs[pos] == '(':
                stack += 1
            elif exprs[pos] == ')':
                stack -= 1
            pos += 1
        return pos

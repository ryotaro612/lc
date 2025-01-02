# https://dai1741.github.io/maximum-algo-2012/docs/parsing/
from collections import deque, defaultdict

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        eval_map = defaultdict(int)

        for i in range(len(evalvars)):
            eval_map[evalvars[i]] = evalints[i]
        
        que = deque(expression)

        res_map, res_num = self.expr(que, eval_map)
        return self.format(res_map, res_num)
    
    def format(self, res_map, num):
        res = []
        for k in sorted(res_map, key=lambda x: (-len(x.split('*')), x.split('*'))):
            if res_map[k]:
                res.append(str(res_map[k]) + '*' + k)
        
        if num:
            res.append(str(num))

        return res

    def expr(self, que, eval_map):
        l_map, l_num = self.term(que, eval_map)

        while True:
            c = None
            while que:
                c = que.popleft()
                if c != ' ':
                    break
            if c is None:
                return l_map, l_num
            
            if c not in {'+', '-'}:
                que.appendleft(c)
                return l_map, l_num
            #print(que, eval_map)
            r_map, r_num = self.term(que, eval_map)
            # print(r_map, r_num)
            if c == '-':
                for k in r_map:
                    r_map[k] = -r_map[k]
                
                r_num = -r_num
            
            l_map, l_num = self.merge(l_map, l_num, r_map, r_num)
    
    def term(self, que, eval_map):
        l_map, l_num = self.factor(que, eval_map)

        while True:
            c = None
            while que:
                c = que.popleft()
                if c != ' ':
                    break
            if c is None:
                return l_map, l_num
            if c != '*':
                que.appendleft(c)
                return l_map, l_num 
            
            r_map, r_num = self.factor(que, eval_map)
            l_map, l_num = self.multi_merge(l_map, l_num, r_map, r_num)
    
    def factor(self, que, eval_map):
        c = ' '    
        while c == ' ':
            c = que.popleft()
    
        if c == '(':
            res, num = self.expr(que, eval_map)
            while que[0] != ')':
                que.popleft()
            que.popleft()
            return res, num
        
        while que and que[0] not in {' ', '+', '-', '*', '(', ')'}:
            c += que.popleft()
        
        if c in eval_map:
            return dict(), eval_map[c]
        if c.isdigit():
            return dict(), int(c)
        
        return {c: 1}, 0

    def multi_merge(self, left, left_num, right, right_num):

        res = defaultdict(int)
        for lk, lv in left.items():
            for rk, rv in right.items():
                key = lk.split('*') + rk.split('*')
                key = '*'.join(sorted(key))
                res[key] += lv * rv
        
        for lk, lv in left.items():
            res[lk] += lv * right_num

        for rk, rv in right.items():
            res[rk] += rv * left_num
               
        return res, left_num * right_num

    def merge(self, left, left_num, right, right_num):
        res = defaultdict(int)
        for k in left:
            res[k] = left[k]
        
        for k, v in right.items():
            res[k] += v
        
        return res, left_num + right_num

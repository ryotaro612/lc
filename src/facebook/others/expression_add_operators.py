"""
"105"
5

"3456237490"
9191

"00"
0
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        dp_mul = [[None for _ in range(n+1)] for _ in range(n+1)]
        dp_pn = [[None for _ in range(n+1)] for _ in range(n+1)]
        return [expr for expr, v in self.listPn(0, n, dp_mul, dp_pn, num) if v == target]
        #for e in sorted(self.listPn(0, n, dp_mul, dp_pn, num), key=lambda x: x[0]):
        #    print(e)
        #return []
    
    def listPn(self, begin: int, end: int, dp_mul, dp_pn, num: str):
        if dp_pn[begin][end] is not None:
            return dp_pn[begin][end]
        
        result = self.listMul(begin, end, dp_mul, num)
        if begin + 1 == end:
            dp_pn[begin][end] = self.listMul(begin, end, dp_mul, num)
            return dp_pn[begin][end]        
        
        for i in range(begin+1, end):
            left = self.listPn(begin, i, dp_mul, dp_pn, num)
            right = self.listMul(i, end, dp_mul, num)
            for expr_l, v_l in left:
                for expr_r, v_r in right: 
                    result.append((f'{expr_l}+{expr_r}', v_l + v_r))
                    result.append((f'{expr_l}-{expr_r}', v_l - v_r))
        return result
    
    def listMul(self, begin: int, end: int, dp_mul, num: str):
        if dp_mul[begin][end] is not None:
            return dp_mul[begin][end]
        
        if begin + 1 == end:
            dp_mul[begin][end] = [(num[begin:end], int(num[begin:end]))]
            return dp_mul[begin][end]
        
        result = []
        if num[begin] == '0':
            result = []
        else:
            result = [(num[begin:end], int(num[begin:end]))]
        for i in range(begin+1, end):
            left = self.listMul(begin, i, dp_mul, num)
            right = num[i:end]
            for expr_l, v in left:
                if not (1 < len(right) and right[0] == '0'): 
                    result.append((f'{expr_l}*{right}', v * int(right)))
        return result
            

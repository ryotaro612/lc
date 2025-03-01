class Solution:
    def minimizeResult(self, expression: str) -> str:
        """
        i_p
        n = len(expression)
        [0..i_p], [i_p+1..n]
        """
        result = float('inf')
        i_p = expression.find('+')
        n = len(expression)

        for i in range(i_p):
            for j in range(i_p+1, n):
                new_expr = []
                if i == 0:
                    p_left = int(expression[:i_p])
                    m_left = 1
                    new_expr.append('(' + expression[:i_p])
                else:
                    p_left = int(expression[i:i_p])
                    m_left = int(expression[:i])
                    
                    new_expr.append(expression[:i] + '(' + expression[i:i_p])
                
                new_expr.append('+')
                
                if j < n - 1:
                    p_right = int(expression[i_p+1:j+1])
                    m_right = int(expression[j+1:])
                    
                    new_expr.append(expression[i_p+1:j+1])
                    new_expr.append(')')
                    new_expr.append(expression[j+1:])
                else:
                    p_right = int(expression[i_p+1:])
                    m_right = 1
                    new_expr.append(expression[i_p+1:])
                    new_expr.append(")")

                cand = m_left * (p_left + p_right) * m_right
                if cand < result:
                    result = cand
                    result_expr = ''.join(new_expr)

        return result_expr

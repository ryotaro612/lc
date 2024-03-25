class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        cache = dict()
        return self.rec(nums, 0, len(nums), cache)[1]

    def rec(self, nums, left, right, cache):
        """
        [left, right)
        -> flat, string
        """
        key = (left, right) 
        if key in cache:
            return cache[key]
        
        if left + 1 == right:
            cache[key] = [nums[left], str(nums[left]), nums[left], str(nums[left])]
            return cache[key]

        result = [-float('inf'), "", float('inf'), ""]
        
        for i in range(left+1, right):
            l_mx, l_mx_expr, l_mn, l_mn_expr = self.rec(nums, left, i, cache)
            r_mx, r_mx_expr, r_mn, r_mn_expr = self.rec(nums, i, right, cache)
            #if left + 1 < i:
            #    l_mx_expr = self.enclose(l_mx_expr)
            #   l_mn_expr = self.enclose(l_mn_expr)
            if i + 1 < right:
                r_mx_expr = self.enclose(r_mx_expr)
                r_mn_expr = self.enclose(r_mn_expr)

            if result[0] < l_mx / r_mn:
                result[0] = l_mx / r_mn
                result[1] = f"{l_mx_expr}/{r_mn_expr}"
            if l_mn / r_mx < result[2]:
                result[2] = l_mn / r_mx
                result[3] = f"{l_mn_expr}/{r_mx_expr}" 
                
        cache[(left, right)] = result
        return result

    def enclose(self, expr):
        return f"({expr})"

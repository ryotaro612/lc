"""
[75027,58436,95472,89426,10786,32325,99823,33237]
5
"""
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        return self.distribute(0, cookies, distribution, k, 0, k)
     
    def distribute(self, i, cookies, distribution, k, max_idx, num_zero):
        n = len(cookies)
        if i == n:
            return distribution[max_idx]
        
        if n - i < num_zero:
            return float('inf')
        
        res = float('inf')
        for j in range(k):
            if distribution[j] == 0:
                num_zero -= 1
            distribution[j] += cookies[i]
            temp = max_idx
            if distribution[temp] <= distribution[j]:
                temp = j
            res = min(res, self.distribute(i+1, cookies, distribution, k, temp, num_zero))
            distribution[j] -= cookies[i]
            if distribution[j] == 0:
                num_zero += 1
        return res

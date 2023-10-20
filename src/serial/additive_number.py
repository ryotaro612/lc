"""
"1023"
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                    pred1 = int(num[:i])
                    pred2 = int(num[i:j])  
                    if str(pred1) == num[:i] and str(pred2) == num[i:j] and self.find(pred1, pred2, j, num):
                        return True
        return False
    
    def find(self, pred1, pred2, start, num):        
        n = len(num)
        for i in range(start+1, n+1):
            pred3 = int(num[start:i])
            if str(pred3) == num[start:i] and pred1 + pred2 == pred3:
                if i == n or self.find(pred2, pred3, i, num):
                    return True
            if pred1 + pred2 < pred3:
                return False
        return False

        

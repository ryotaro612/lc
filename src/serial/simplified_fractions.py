class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        """
        denom [2..n]
        num [1,..denom-1]
        result = set()
        """

        result = set()

        for denom in range(2, n+1):
            for num in range(1, denom):
                d = denom
                while True:
                    g = self.gcd(d, num)
                    
                    if g == 1:
                        break
                    d //= g
                    num  //= g
                
                result.add((num, d))
        
        return [f"{num}/{denom}" for num, denom in result]

    
    def gcd(self, a, b):
        if b > a:
            return self.gcd(b, a)
        
        if b == 0:
            return a
        
        return self.gcd(b, a % b)

class Solution:
    def confusingNumberII(self, n: int) -> int:
        s = str(n)
        length = len(s)
        dp = [[0] * 2 for _ in range(length + 1)]
        dp[0][0] = 1
        
        for i, c in enumerate(s):
            d = ord(c) - ord('0')
            
            rotate_d = [0, 1, 6, 8, 9]
        
            if d in rotate_d:
                dp[i+1][0] = dp[i][0]
                
            n_small = len([e for e in rotate_d if e < d])
            
            dp[i+1][1] += dp[i][0] * n_small
            dp[i+1][1] += dp[i][1] * len(rotate_d)
        
        palindromes = self.generate_palindromes(n)
        # print(palindromes)
        return dp[length][0] + dp[length][1] - len(palindromes) - 1
    
    def generate_palindromes(self, n):
        
        length = len(str(n))
        memo = dict()
        return list({
            int(v)
            for l
            in range(1, length + 1)
            for v
            in self.generate(l, memo)
            if int(v) <= n and not v.startswith('0')
        })
        
    def generate(self, length, memo):
        if length in memo:
            return memo[length]
        
        if length == 1:
            return ['0', '1', '8']
        elif length == 2:
            return ['00', '11', '88', '96', '69']
        elif length % 2:
            substrs = self.generate(length - 1, memo)
            result = []
            for sub in substrs:
                for mid in ['0', '1', '8']:
                    result.append(sub[:(length-1)//2] + mid + sub[(length-1)//2:])
            memo[length] = result
            return memo[length]
        else:
            substrs = self.generate(length - 2, memo)
            result = []
            for sub in substrs:
                for e in ['0' + sub + '0', '1' + sub + '1', '8' + sub + '8', '6' + sub + '9', '9' + sub + '6']:
                    result.append(e)
            memo[length] = result
            return memo[length]

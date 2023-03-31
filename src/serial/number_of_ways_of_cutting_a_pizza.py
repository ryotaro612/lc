class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        n_r = len(pizza)
        n_c = len(pizza[0])
        sum_matrix = [[0] * n_c for _ in range(n_r)]
        for r in range(n_r):
            for c in range(n_c):
                if pizza[r][c] == 'A':
                    sum_matrix[r][c] = 1
                if r:
                    sum_matrix[r][c] += sum_matrix[r-1][c]
                if c:
                    sum_matrix[r][c] += sum_matrix[r][c-1]
                if r and c:
                    sum_matrix[r][c] -= sum_matrix[r-1][c-1]

        dp = [[[-1] * (k+1) for _ in range(n_c)] for _ in range(n_r)]
        
        return self.count(0, 0, dp, sum_matrix, k)
    
    def count(self, r, c, dp, sum_matrix, k):
        n_r = len(dp)
        n_c = len(dp[0])

        if dp[r][c][k] != -1:
            return dp[r][c][k]

        if k == 1:
            if self.countApples(r, c, n_r-1, n_c-1, sum_matrix):
                return 1
            else:
                return 0

        mod = 1000000000 + 7
        result = 0 
        for i in range(r, n_r-1):
            if self.countApples(r, c, i, n_c-1, sum_matrix):
                sub = self.count(i+1, c, dp, sum_matrix, k-1)
                if sub:
                    result += sub
                    result %= mod
        for i in range(c, n_c-1):
            if self.countApples(r, c, n_r-1, i, sum_matrix):
                sub = self.count(r, i+1, dp, sum_matrix, k-1)
                if sub:
                    result += sub
                    result %= mod
        
        dp[r][c][k] = result
        # print(r, c, k, ' -> ',result)
        return dp[r][c][k]

    def countApples(self, r1, c1, r2, c2, sum_prefix):
        result = sum_prefix[r2][c2]
        if c1 > 0:
            result -= sum_prefix[r2][c1-1]
        if r1 > 0:
            result -= sum_prefix[r1-1][c2]
        if c1 and r1:
            result += sum_prefix[r1-1][c1-1]
        # print(r1, c1, r2, c2, result, 'apple')
        return result

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """

        sort socres and ages by scores
        n = len(scores)
        dp[i][j]  0<=i<n, 0<=j<1001
        dp[i][j]
        dp[n][max(ages)]
        dp[i][j] = dp[i-1][j] + scores[i] if ages[i] <= j
                =  dp[i-1][j] otherwise
               =  dp[i][j-1]
        """
        max_age = max(ages)
        tuples = sorted(zip(scores, ages), reverse=True)
        scores = [t[0] for t in tuples]
        ages = [t[1] for t in tuples]
        #print('scores', scores)
        #print('ages  ', ages)
        n = len(tuples)
        dp = [[-float('inf')] * (max_age+1) for _ in range(n+1)]
        dp[0] = [0] * (max_age + 1)

        for i in range(n):
            for j in range(max_age+1):
                dp[i+1][j] = dp[i][j]
            for j in range(max_age, -1, -1):
                if ages[i] <= j:
                    dp[i+1][ages[i]] = max(dp[i+1][ages[i]], dp[i][j] + scores[i])

        #for row in dp:
        #    print(row)
        return max(dp[n])

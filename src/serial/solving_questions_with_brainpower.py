class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-float('inf')] * n

        return self.calc(0, dp, questions)

    def calc(self, i, dp, questions):
        n = len(questions)
        if i >= n:
            return 0
        if dp[i] >= 0:
            return dp[i]

        point, brain = questions[i]

        dp[i] = max(self.calc(i+1, dp, questions), point + self.calc(i+brain+1, dp, questions))

        return dp[i]
        

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.sub(rating) + self.sub(rating[::-1])
        
    def sub(self, rating):
        n = len(rating)
        n_rating = [0] * n
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    n_rating[i] += 1
        result = 0
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    result += n_rating[j]
        return result

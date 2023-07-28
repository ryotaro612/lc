class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        cache = dict()
        score1, score2 = self.simulate(nums, 0, len(nums), cache)
        return score1 >= score2

    def simulate(self, nums, left, right, cache):
        """
        [left, right)
        """
        key = (left, right)
        if key in cache:
            return cache[key]

        if left == right:
            cache[key] = [0, 0]
            return cache[key]
        
        head_score2, head_score1 = self.simulate(nums, left+1, right, cache)
        tail_score2, tail_score1 = self.simulate(nums, left, right-1, cache)
        if head_score1 + nums[left] - head_score2 >= tail_score1 + nums[right-1] - tail_score2:
            cache[key] = [head_score1 + nums[left], head_score2]
        else:
            cache[key] = [tail_score1 + nums[right-1], tail_score2]
        return cache[key]
        

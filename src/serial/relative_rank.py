class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = sorted(score, reverse=True)
        score_rank = dict()
        for rank, s in enumerate(sorted(score, reverse=True)):
            score_rank[s] = rank + 1

        result = []
        for s in score:
            if score_rank[s] == 1:
                result.append('Gold Medal')
            elif score_rank[s] == 2:
                result.append('Silver Medal')
            elif score_rank[s] == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(score_rank[s]))

        return result

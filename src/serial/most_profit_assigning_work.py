import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n_jobs = len(difficulty)
        diff_prof = [[d, -p] for d, p in zip(difficulty, profit)]
        diff_prof.sort()
        
        diff_max_profit = [[diff_prof[0][0], -diff_prof[0][1]]]
        for d, neg_p in diff_prof[1:]:
            if diff_max_profit[-1][0] == d:
                continue
            diff_max_profit.append([d, max(-neg_p, diff_max_profit[-1][1])])

        result = 0
        # print(diff_max_profit)
        for w in worker:
            found = bisect.bisect_right(diff_max_profit, [w, float('inf')])
            if found:
                result += diff_max_profit[found-1][1]
        
        return result

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n_col = target + 1
        current = [list() for _ in range(n_col)]
        for candidate in candidates:
            for sum_val in range(n_col):
                result = []
                if sum_val == candidate:
                    result.append([candidate])
                if 0 < sum_val - candidate:
                    for combi in current[sum_val - candidate]:
                        result.append(combi + [candidate])
                current[sum_val].extend(result)                    
        return current[target]    

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        lb = 0
        total = sum(sweetness)
        n = len(sweetness)
        ub = total + 1
        if k == 0:
            return total
        while ub - lb  > 1:
            mid = (ub + lb) // 2

            n_cut = 0
            run_sum = 0
            ok = False
            for i in range(n):
                item = sweetness[i]
                run_sum += item
                if run_sum >= mid:
                    run_sum = 0
                    n_cut += 1
                    if n_cut == k:
                        ok = sum(sweetness[i+1:]) >= mid
            if ok:
                lb = mid
            else:
                ub = mid
        return lb

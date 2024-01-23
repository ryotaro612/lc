class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.rec(0, arr, set())

    def rec(self, i, arr, used) -> int:
        if i == len(arr):
            return 0
        res = 0
        new_used = set(used)
        for c in arr[i]:
            if c in new_used:
                break
            new_used.add(c)
        else:
            res = len(arr[i]) + self.rec(i+1, arr, new_used)
        
        res = max(res, self.rec(i+1, arr, used))
        return res

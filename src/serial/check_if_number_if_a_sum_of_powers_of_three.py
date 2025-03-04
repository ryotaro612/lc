class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        lst = []
        i = 0
        while len(lst) == 0 or lst[-1] < n:
            lst.append(3**i)
            i += 1
        
        for mask in range(1<<len(lst)):
            cand = 0
            for i in range(len(lst)):
                if mask & (1<<i):
                    cand += lst[i]
            if cand == n:
                return True
        
        return False

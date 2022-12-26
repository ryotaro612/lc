from collections import defaultdict
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = dict()
        return self.rec(s1, s2, memo)
    def rec(self, s1, s2, memo):
        key = (s1, s2)
        if key in memo:
            return memo[key]
        if s1 == s2:
            memo[key] = True
            return memo[key]
        if len(s1) == 1:
            memo[key] = False
            return memo[key]

        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        counter2_rev = defaultdict(int)
        n = len(s1)
        for i in range(n-1):
            counter1[s1[i]] += 1
            counter2[s2[i]] += 1
            counter2_rev[s2[n-1-i]] += 1

            if counter1 == counter2:
                memo[key] = self.rec(s1[:i+1], s2[:i+1], memo) and self.rec(s1[i+1:], s2[i+1:], memo)
                if memo[key]:
                    return True

            if counter1 == counter2_rev:
                memo[key] = self.rec(s1[:i+1], s2[n-1-i:n], memo) and self.rec(s1[i+1:], s2[:n-1-i], memo)
                if memo[key]:
                    return True
        memo[key] = False
        return memo[key]

from collections import deque

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ques = [deque() for _ in range(3)]
        n = len(s)

        for i, c in enumerate(s):
            ques[ord(c) - ord('a')].append(i)
        result = 0

        for i in range(n):
            if len([q for q in ques if q]) == 3:
                l = max([q[0] for q in ques])
                result += n - l

            for q in ques:
                while q and q[0] <= i:
                    q.popleft()

        return result

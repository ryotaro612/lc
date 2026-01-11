from bisect import bisect_left
from collections import defaultdict
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        """
        counter[]
        result = []
        """
        counter = defaultdict(int)
        n = len(times)
        self.result = [0] * n
        self.result[0] = persons[0]
        elected = persons[0]
        counter[persons[0]] += 1

        for i in range(1, n):
            counter[persons[i]] += 1
            if counter[elected] <= counter[persons[i]]:
                elected = persons[i]

            self.result[i] = elected
        self.times = times

    def q(self, t: int) -> int:
        n = len(self.times)
        idx = bisect_left(self.times, t)
        if idx == n:
            return self.result[-1]
        
        if self.times[idx] == t:
            return self.result[idx]
        
        return self.result[idx-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

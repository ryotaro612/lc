from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)

        num_freq = [[n, f] for n, f in counter.items()]

        result = []

        self.collect(0, num_freq, [], result)

        return result

    def collect(self, idx, num_freq, current, result):
        n = len(num_freq)
        if idx == n:
            result.append(list(current))
            return
        v = num_freq[idx][0]
        for count in range(num_freq[idx][1] + 1):

            self.collect(idx+1, num_freq, current, result)
            current.append(v)
        
        while current and current[-1] == v:
            current.pop()
            

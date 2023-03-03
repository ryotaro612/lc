from collections import defaultdict

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        if len([v for v in counter.values() if v % 2]) > 1:
            return []

        middle = ''
        for c in counter:
            if counter[c] % 2:
                middle = c
                counter[c] -= 1

        result = []
        self.backtrack(counter, [], result, middle)
        return result

    def backtrack(self, counter, running, result, middle):
        if [k for k in counter if counter[k]]:
            for c in counter:
                if counter[c]:
                    running.append(c)
                    counter[c] -= 2
                    self.backtrack(counter, running, result, middle)
                    running.pop()
                    counter[c] += 2
        else:
            first = ''.join(running)
            result.append(first + middle + first[::-1])

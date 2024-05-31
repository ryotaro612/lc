class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        return self.rec({'1' * n}, presses)

    def rec(self, patterns, presses):
        if presses == 0:
            return len(patterns)
        
        next_patterns = set()
        for pattern in patterns:
            next_patterns.add(self.gen(pattern, lambda _: True))
            next_patterns.add(self.gen(pattern, lambda i: i % 2))
            next_patterns.add(self.gen(pattern, lambda i: i % 2 == 0))
            next_patterns.add(self.gen(pattern, lambda i: i % 3 == 0))
        # print(next_patterns)
        return self.rec(next_patterns, presses - 1)

    def gen(self, pattern, flip):
        result = []
        for i, c in enumerate(pattern):
            if flip(i):
                e = '1' if c == '0' else '0'
            else:
                e = c
            result.append(e)
        return ''.join(result)

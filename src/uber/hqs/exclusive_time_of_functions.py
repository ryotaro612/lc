"""
2
["0:start:0","1:start:2","1:end:5","0:end:6"]

2
["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        n_logs = len(logs)
        stack = []
        current = 0
        for i in range(n_logs):
            func, start_end, timestamp = self.tokenize(logs[i])
            if start_end == 'start':
                if len(stack) > 0:
                    result[stack[-1]] += timestamp - current
                current = timestamp
                stack.append(func)
            else:
                result[stack.pop()] += timestamp - current + 1
                current = timestamp + 1
        return result
    def tokenize(self, log):
        function, start_end, timestamp = log.split(':')
        return int(function), start_end, int(timestamp)

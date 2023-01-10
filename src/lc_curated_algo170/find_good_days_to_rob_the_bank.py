class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        non_inc = self.find_non_inc(security, time)
        n = len(security)
        non_dec = {n - 1 - i for i in self.find_non_inc(security[::-1], time)}
        return list(non_inc & non_dec )

    def find_non_inc(self, security, time):
        n = len(security)
        stack = []
        # stack[i] >= stack[i+1]
        result = set()
        for i in range(n):
            if stack:
                if stack[-1] >= security[i]:
                    stack.append(security[i])
                else:
                    stack = [security[i]]
            else:
                stack.append(security[i])

            if len(stack) > time:
                result.add(i)
        return result

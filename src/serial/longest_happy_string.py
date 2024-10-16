class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counter = {'a': a, 'b': b, 'c': c}
        while counter['a'] or counter['b'] or counter['c']:
            order = sorted(list(counter.keys()), reverse=True, key=lambda i: counter[i])
            # print(counter, order, result)
            if len(result) < 2 or not (result[-2] == result[-1] == order[0]):
                result.append(order[0])
                counter[order[0]] -= 1
            elif counter[order[1]] > 0:
                result.append(order[1])
                counter[order[1]] -= 1
            else:
                return ''.join(result)
        return ''.join(result)
            

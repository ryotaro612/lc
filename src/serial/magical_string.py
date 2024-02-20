class Solution:
    def magicalString(self, n: int) -> int:
        lst = self.generate(n)
        # print(lst)
        return len([v for v in lst if v == 1])
    
    def generate(self, n):
        result = [1, 2, 2]
        cur = 2
        while len(result) < n:
            if result[cur] == 1:
                if result[-1] == 1:
                    result.append(2)
                else:
                    result.append(1)
            else:
                if result[-1] == 1:
                    result.extend([2, 2])
                else:
                    result.extend([1, 1])
            cur += 1
        return result[:n]

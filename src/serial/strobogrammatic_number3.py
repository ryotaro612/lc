"""
"0"
"1680"
"""
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        if high == '0':
            return 1
        return self.count_strobo_nums(high) - self.count_strobo_nums(str(int(low) - 1))

    def count_strobo_nums(self, v):
        if int(v) < 0:
            return 0
        # print('count strobo', v)
        same = self.count_same_len_strobo_nums(v, [])
        less = 0
        for i in range(1, len(v)):
            if i == 1:
                less += 3
            else:
                if i % 2:
                    less += 4 * int(5 ** (i // 2 - 1)) * 3
                else:
                    less += 4 * int(5 ** (i // 2 - 1))
        # print(same, less, same + less)
        return same + less

    def count_same_len_strobo_nums(self, v, prefix):
        n = len(v)
        
        if len(prefix) == n // 2:
            num = int(v)
            rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
            suffix = [rotate[d] for d in prefix[::-1]]
            result = 0
            if n % 2:
                for d in [0, 1, 8]:
                    if num >= int(''.join([str(c) for c in prefix + [d] + suffix])):
                        result += 1
                return result
            else:
                if num >= int(''.join([str(c) for c in prefix + suffix])):
                    # print(int(''.join([str(c) for c in prefix + suffix])))
                    return 1
                else:
                    return 0
        else:
            result = 0
            digits = [1, 6, 8, 9]
            if prefix:
                digits.append(0)
            for i in digits:
                prefix.append(i)
                result += self.count_same_len_strobo_nums(v, prefix)
                prefix.pop()
            return result
        


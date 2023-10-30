class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        100 123
        9*9*8
        i
        9*9*7...*(9-i+1)
        """
        if n == 0:
            return 1

        result = 10
        for i in range(2, n+1):
            n_pattern = 9
            count = 9
            for _ in range(i-1):
                n_pattern *= count
                count -= 1
            result += n_pattern
        return result

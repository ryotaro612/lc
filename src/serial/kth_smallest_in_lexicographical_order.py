class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 0
        acc = 0
        while True:
            for d in range(0 if prefix else 1, 10):
                num = self.count(n, prefix * 10 + d)
                # print(num, acc, prefix*10+d)
                if k <= acc + num:
                    prefix = prefix * 10 + d
                    acc += 1
                    if acc == k:
                        return prefix
                    else:
                        break
                acc += num

    def count(self, n, prefix):
        # print(n, prefix)
        if n < prefix:
            return 0
        res = 1
        if str(prefix) < str(n)[:len(str(prefix))]:
            for i in range(len(str(n)) - len(str(prefix))):
                res += 10 ** (i+1)
            return res
        if str(prefix) == str(n)[:len(str(prefix))]:
            for i in range(10):
                res += self.count(n, prefix*10 + i)
            return res
        else:
            for i in range(len(str(n)) - len(str(prefix)) - 1):
                res += 10 ** (i+1)
            return res

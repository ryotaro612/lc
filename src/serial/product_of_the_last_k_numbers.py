class ProductOfNumbers:

    def __init__(self):
        self.list  = []        

    def add(self, num: int) -> None:
        if self.list and self.list[-1][0] == num:
            self.list[-1][1] += 1
        else:
            self.list.append([num, 1])

    def getProduct(self, k: int) -> int:
        res = 1
        i = -1
        while k > 0:
            if self.list[i][0] == 0:
                return 0
            elif self.list[i][0] == 1:
                k -= self.list[i][1]
            else:
                for a in range(self.list[i][1]):
                    res *= self.list[i][0]
                    k -= 1
                    if k == 0:
                        return res
            i -= 1
        return res
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

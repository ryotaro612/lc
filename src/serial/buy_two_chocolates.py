class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        cost =  prices[0] + prices[1]
        if money < cost:
            return money
        else:
            return money - cost

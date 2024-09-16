class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.time = 0
        self.product_price = {product: price for product, price in zip(products, prices)}


    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.time += 1
        result = 0
        for p, a in zip(product, amount):
            result += self.product_price[p] * a

        if self.time % self.n:
            return result
        
        return result * (100-self.discount) / 100 


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

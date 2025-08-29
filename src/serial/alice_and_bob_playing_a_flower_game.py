class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        (x, y) -> (x + y) % 2 = 1
        x -> odd y -> even
        x -> even y -> odd
        """
        return self.count_odd(n) * self.count_even(m) + self.count_even(n) * self.count_odd(m)

    
    def count_even(self, n):
        """
        [1, n]
        n =1 -> 0
        n = 2 -> 1
        n = 3 -> 1
        n = 4 -> 2
        """
        return n // 2
    
    def count_odd(self, n):
        return n - self.count_even(n)

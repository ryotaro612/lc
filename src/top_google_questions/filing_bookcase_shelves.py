class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n_books = len(books)
        dp = [[float('inf')] * (shelfWidth+1) for _ in range(len(books) + 1)]

        return self.rec(0, 0, 0, dp, books, shelfWidth)

    def rec(self, i, w, h, dp, books, shelf_width):
        n_books = len(books)
        if i == n_books:
            return h
        
        if dp[i][w] < float('inf'):
            return dp[i][w]
        
        dp[i][w] = h + self.rec(i+1, books[i][0], books[i][1], dp, books, shelf_width)
        if w + books[i][0] <= shelf_width:
            dp[i][w] = min(dp[i][w], self.rec(i+1, w+books[i][0], max(h, books[i][1]), dp, books, shelf_width))
        return dp[i][w]

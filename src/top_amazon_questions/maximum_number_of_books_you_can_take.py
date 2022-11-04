"""
[1,3,3]

[14,2,12,6,2,12,13]
"""
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        stack = [0]
        dp = [0] * n
        dp[0] = books[0]
        
        for i in range(1, n):
            if books[i] > books[i-1]:
                dp[i] = dp[i-1] + books[i]
                
            else:
                while stack:
                    j = stack[-1]
                    if books[i] - (i-j) < books[j]:
                        stack.pop()
                    else:
                        break
            
                if stack:
                    j = stack[-1]
                    dp[i] = dp[j] + (books[i] + (books[i] - (i-j-1))) * (i-j) // 2
                elif books[i] - i >= 0:
                    dp[i] = (i+1) * (books[i] + books[i] - i) // 2
                else:
                    dp[i] = books[i] * (books[i] + 1) // 2
            stack.append(i)
        print(dp)
        return max(dp)

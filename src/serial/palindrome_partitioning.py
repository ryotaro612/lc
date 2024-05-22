class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cache = dict()
        return self.rec(s, cache)

    def rec(self, s, cache):
        if s in cache:
            return cache[s]
        if not s:
            cache[s] = []
            return cache[s]
        
        n = len(s)
        result = []
        if self.is_palindrome(s):
            result.append([s])
        for pivot in range(1, n):
            first = self.rec(s[:pivot], cache)
            if self.is_palindrome(s[pivot:]):
                for chunk in first:
                    result.append(list(chunk) + [s[pivot:]])
        cache[s] = result
        return cache[s]

    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

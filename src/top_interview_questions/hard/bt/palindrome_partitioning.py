class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.sub_partition(s, 0, len(s))
        
    def sub_partition(
        self, s: str, start: int, end: int) -> list[list[str]]:

        result: list[list[str]] = []
            
        if self.is_palindrome(s, start, end):
            result.append([s[start:end]])
        
        for i in range(start+1, end):
            if self.is_palindrome(s, start, i):
                left_p = [s[start:i]]
                right = self.sub_partition(s, i, end)
                for right_p in right:
                    result.append(left_p + right_p)

        return result
        
    def is_palindrome(self, s, start, end):
        i = 0
        while start + i <= end-1 - i:
            if s[start+i] != s[end - 1 - i]:
                return False
            i += 1
        return True

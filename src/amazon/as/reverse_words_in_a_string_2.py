class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        self.reverse(s, 0, n)   
        start = 0
        end = 0
        while True:
            if end == n or s[end] == ' ':
                self.reverse(s, start, end)
                end += 1
                start = end
                if n <= end:
                    break
            else:
                end += 1
    
    def reverse(self, s: List[str], start, end):
        for i in range(start, end):
            if i < end - 1 - (i - start):
                temp = s[i]
                s[i] = s[end - 1 - (i - start)]
                s[end-1-(i-start)] = temp
            else:
                break
        

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)
        # s = "abb"
        for i in range(n):
            if n - 2 <= i:
                break;
            if len({s[i], s[i+1], s[i+2]}) != 1:
                continue;
            if not (i == 0 or s[i-1] != s[i]):
                continue;

            start = i
            end = i+2
            while end < n -1 and s[end] == s[end+1]:
                end += 1
            result.append([start, end])
            
        return result

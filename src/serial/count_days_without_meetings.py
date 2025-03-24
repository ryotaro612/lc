class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        n = len(meetings)
        spans = []
        i = 0
        while i < n:
            if not spans:
                spans.append(meetings[i])
                i += 1
            else:
                if spans[-1][0] <= meetings[i][0] <=spans[-1][1]:
                    spans[-1][1] = max(spans[-1][1], meetings[i][1])
                else:
                    spans.append(meetings[i])
                i += 1
        
        result = days
        for a, b in spans:
            result -= b - a + 1
        
        return result
        

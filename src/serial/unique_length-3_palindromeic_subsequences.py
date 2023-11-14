import bisect

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pos_list = [[] for _ in range(26)]
        
        for i, c in enumerate(s):
            pos_list[ord(c) - ord('a')].append(i)
        
        result = 0
        for edge_c in range(26):
            if len(pos_list[edge_c]) < 2:
                continue
            left, right  = pos_list[edge_c][0], pos_list[edge_c][-1]
            for mid in range(26):
                if mid == edge_c:
                    if len(pos_list[edge_c]) >= 3:
                        result += 1
                else:
                    if bisect.bisect_left(pos_list[mid], left) != bisect.bisect_left(pos_list[mid], right):
                        result += 1
        return result

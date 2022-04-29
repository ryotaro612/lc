class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_count = dict()
        for c in p:
            char_count[c] = char_count.get(c, 0) + 1
        
        result = []
        window_count = dict()
        for char in char_count.keys():
            window_count[char]= 0
        tail = 0
        for head in range(len(s)):
            tail = max(head, tail)
            while tail < len(s) and s[tail] in char_count:
                c = s[tail]
                if window_count[c] < char_count[c]:
                    window_count[c] += 1
                    tail += 1
                    if tail - head == len(p):
                        result.append(head)
                        break
                else:
                    break
            if s[head] in char_count:
                window_count[s[head]] -= 1
        return result

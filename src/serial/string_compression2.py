class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = dict()
        return min([self.count_len(pattern) for pattern in self.find_min(s, 0, k, cache)])
    
    def find_min(self, s, pos, k, cache):
        key = (pos, k)
        if key in cache:
            return cache[key]

        n = len(s)
        if pos == n:
            cache[key] = [[0, 0] for _ in range(26)]
            return cache[key]
        
        result = [[0, float('inf')] for _ in range(26)]
        
        sub_result = self.find_min(s, pos+1, k, cache)
        c_i = ord(s[pos]) - ord('a')
        result[c_i] = [1 + sub_result[c_i][0], sub_result[c_i][1]]
        for i in range(26):
            if i != c_i:
                if sub_result[i][0] == 1:
                    temp = [1, 1 + sub_result[i][1]]
                else:
                    temp = [1, 1 + len(str(sub_result[i][0])) + sub_result[i][1]]
                if self.count_len(result[c_i]) > self.count_len(temp):
                    result[c_i] = temp
        
        if k:
            for i, pattern in enumerate(self.find_min(s, pos+1, k-1, cache)):
                if self.count_len(result[i]) > self.count_len(pattern):
                    result[i] = pattern
               
        cache[key] = result
        
        # print(s[pos:], k , cache[key])
        return cache[key]

    def count_len(self, v):
        if v[0] == 0:
            return v[1]
        if v[0] == 1:
            return 1 + v[1]
        else:
            return 1 + len(str(v[0])) + v[1]

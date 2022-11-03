"""
aabbbaaaa
*

count = 0
count -= 1 if b

"lripaa"

"""
class Solution:
    def largestVariance(self, s: str) -> int:
        
        positions = [[] for _ in range(26)]
        for i, c in enumerate(s):
            positions[ord(c) - ord('a')].append(i)
        
        result = 0
        for i in range(25):
            for j in range(i+1, 26):
                c_1 = chr(i + ord('a'))
                c_2 = chr(j + ord('a'))
                sub = []
                
                p_1 = 0
                p_2 = 0
                if not (positions[i] and positions[j]):
                    continue
                
                while p_1 < len(positions[i]) or p_2 < len(positions[j]):
                    
                    if p_1 < len(positions[i]):
                        if p_2 < len(positions[j]):
                            
                            if positions[i][p_1] < positions[j][p_2]:
                                sub.append(c_1)
                                p_1 += 1
                            else:
                                sub.append(c_2)
                                p_2 += 1
                        else:
                            sub.append(c_1)
                            p_1 += 1
                    else:
                        sub.append(c_2)
                        p_2 += 1
                
                rev_sub = sub[::-1]
                result = max(
                    result, 
                    self.count(sub, c_1, c_2), 
                    self.count(sub, c_2, c_1),
                    self.count(rev_sub, c_1, c_2), 
                    self.count(rev_sub, c_2, c_1)
                )
        
        return result
    
    
    def count(self, sub, c_1, c_2):
        # print(sub)
        result = 0
        l_set = set()
        temp = 0
        for c in sub:
            l_set.add(c)
            if c == c_1:
                temp += 1
                if len(l_set) > 1:
                    result = max(temp, result)
            else:
                if temp >= 1:
                    temp -= 1
                    if len(l_set) > 1:
                        result = max(temp, result)
                else:
                    l_set = set()
        # print(result)
        return result

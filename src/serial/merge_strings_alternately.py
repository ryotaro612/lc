class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        n1 = len(word1)
        n2 = len(word2)
        p1, p2 = 0, 0
        is_word1 = True
        while p1 < n1 or p2 < n2:
            if p1 < n1:
                if p2 < n2:
                    if is_word1:
                        result.append(word1[p1])
                        p1 += 1
                    else:
                        result.append(word2[p2])
                        p2 += 1
                    is_word1 = not is_word1
                else:
                    result.append(word1[p1])
                    p1 += 1
            else:
                result.append(word2[p2])
                p2 += 1
        
        return ''.join(result)

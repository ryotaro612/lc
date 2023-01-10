import bisect
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            pos_list = [i for i, word in enumerate(wordsDict) if word == word1]
            return min([pos_list[i+1] - pos_list[i] for i in range(len(pos_list)-1)])
        
        pos1 = [i for i, word in enumerate(wordsDict) if word == word1]
        pos2 = [i for i, word in enumerate(wordsDict) if word == word2]

        result = float('inf')
        for pos in pos1:
            left = bisect.bisect_left(pos2, pos)
            if left < len(pos2):
                result = min(result, pos2[left] - pos)
            if left:
                result = min(result, pos - pos2[left-1])
        return result

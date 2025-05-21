from collections import defaultdict, Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        total = defaultdict(int)
        for word in words2:
            counter = Counter(word)

            for c, freq in counter.items():
                total[c] = max(total[c], freq)
            
        result = []
        for word in words1:
            counter = defaultdict(int)
            for c in word:
                counter[c] += 1
            
            for c, freq in total.items():
                if counter[c] < freq:
                    break
            else:
                result.append(word)
        
        return result

from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        gg = 1

        result = 0
        result += min([lc], cl) * 2 

        result += val // 2 * 2

        [gg. gg] in words

        result += 2
        """
        counter = Counter(words)
        result = 0
        middle = False
        for word in counter:
            if word[0] == word[1]:
                n_entry = counter[word] // 2 * 2
                result += n_entry * 2
                counter[word] -= n_entry
                
                if counter[word]:
                    middle = True
                continue
            
            n_entry = min(counter[word], counter.get(word[::-1], 0)) 
            counter[word] -= n_entry
            if word[::-1] in counter:
                counter[word[::-1]] -= n_entry
            
            result += n_entry * 2 * 2
        
        return result + 2 if middle else result

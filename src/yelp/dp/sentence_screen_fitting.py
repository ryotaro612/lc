"""
["hello","world"]
2
8
hello---
world---
["a", "bcd", "e"]
3
6
["i","had","apple","pie"]
4
5
["pen", "aa", "bbbb"]
23
5
["a"]
23
5
["a", "ab", "abc"]
8
6

["hi","good","morning","leetcode"]
100
55
["hi","good","morning","leetcode"]
10
20
01234567890123456789
hi good morning
leetcode hi good
morning leetcode hi
good morning
leetcode hi good
morning leetcode hi
good morning
leetcode hi good
morning leetcode hi
good morning
"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        for word in sentence:
            if len(word) > cols:
                return 0
        result = 0
        space = 0
        n = len(' '.join(sentence) + ' ')
        word_idx = 0
        for _ in range(rows):
            space = cols
            if 1 < cols // n:
                result += cols // n - 1
                space -= (cols // n - 1) * n
            while len(sentence[word_idx]) <= space:
                word_len = len(sentence[word_idx])
                space -= word_len
                if word_idx == len(sentence) - 1:
                    result += 1
                word_idx = (word_idx + 1) % len(sentence)
                space -= 1
            
        return result 
                    

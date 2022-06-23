"""
["do", "dd", "doge", "aa", "a"]
4

["This", "is", "an", "example", "of", "text", "justification."]
16

["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
20

"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        index = 0
        lines = [[]]
        num_chars = 0
        n = len(words)
        while index < n:
            if num_chars + len(words[index]) <= maxWidth:
                num_chars += len(words[index]) + 1
                lines[-1].append(words[index])
                index += 1
            else:
                lines.append([])
                num_chars = 0
                
        result = []     
        for i in range(len(lines)-1):
            result.append(self.display(lines[i], maxWidth))

        last = ' '.join(lines[-1])
        result.append(last + ' ' * (maxWidth - len(last)))
 
        return result
    
    def display(self, words, maxWidth):
        n_chars = sum([len(word) for word in words])
        n = len(words)
        if n == 1:
            return words[0] + ' ' * (maxWidth - n_chars)

        even = (maxWidth - n_chars) // (n-1)
        extra = (maxWidth - n_chars) % (n-1)
        line = []
        for i, word in enumerate(words):
            line.append(word)
            if i < n-1:
                line.append(' ' * even)
                if extra > 0:
                    line.append(' ')
                    extra -= 1
        return ''.join(line)

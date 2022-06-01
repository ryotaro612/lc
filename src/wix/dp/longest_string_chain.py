class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        words = list(word_set)
        
        g = dict()
        for word in words:
            g[word] = []
            n = len(word)
            for i in range(n):
                sub = word[:i] + (word[i+1:] if i < n-1 else "")
                if sub in word_set:
                    g[word].append(sub)
        heights = dict()
        result = 1
        for word in words:
            result = max(result, self.count(word, g, heights))
                         
        return result
    
    def count(self, word, g, heights):
        if word in heights:
            return heights[word]

        heights[word] = 1
        for neighbor in g[word]:
            heights[word] = max(heights[word], self.count(neighbor, g, heights) + 1)
        return heights[word]

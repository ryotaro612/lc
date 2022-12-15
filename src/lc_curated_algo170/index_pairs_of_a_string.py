class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        n = len(text)
        result = []
        for word in words:
            n_w = len(word)
            for i in range(n - n_w + 1):
                if word == text[i:i+n_w]:
                    result.append([i, i + n_w - 1])
        return sorted(result)

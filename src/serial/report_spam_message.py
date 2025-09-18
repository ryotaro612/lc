class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        words = set(bannedWords)
        counter = 0
        for word in message:
            if word in words:
                counter += 1
        
        return counter >= 2

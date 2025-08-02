class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        word = list(word)

        result = 0
        n = len(word)
        for i in range(1, n-1):
            if abs(ord(word[i-1]) - ord(word[i])) <= 1 and abs(ord(word[i]) - ord(word[i+1])) <= 1:
                c = 0
                while abs(ord(word[i-1]) - (ord('a')+c)) <= 1 or abs(ord(word[i+1]) - (ord('a') + c)) <= 1:
                    c += 1
                
                word[i] = chr(ord('a') + c)
                result += 1
        # print(word)
        for i in range(n):
            if (i and abs(ord(word[i-1]) - ord(word[i])) <= 1) or ((i < n-1) and abs(ord(word[i]) - ord(word[i+1])) <= 1):
                c = 0
                while (i and abs(ord(word[i-1]) - (ord('a') + c)) <= 1) or ((i <n-1) and abs(ord(word[i+1]) - (ord('a')+c)) <= 1):
                    c += 1
                
                word[i] = chr(ord('a') + c)
                result += 1
        # print(word)
        return result

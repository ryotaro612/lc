class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        # word[i:] # 0<= n-1
        """
        n = 4
        numFriends = 2
        i=0 => word[0:n-1]  n-(numFriend-1) = n-1
        i=1 => word[1:n]
        word[i:j]
        if i <= numFriends-1 word[i:]
        else:
            word[i:j]  i + n-j = numFriend
            j = i+n-numFriends
        """
        if numFriends == 1:
            return word
        result = ""
        for i in range(n):
            if i >= numFriends - 1:
                cand = word[i:]
            else:
                cand = word[i:(i+n-numFriends+1)]
            
            result = max(result, cand)
        
        return result
        
        """
        n = len(word)
        m = n - numFriends + 1
        if numFriends == 1:
            return word
        return max(word[i:i + m] for i in range(n))
        """

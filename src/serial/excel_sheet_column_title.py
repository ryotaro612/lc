class Solution:
    def convertToTitle(self, n: int) -> str:
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return chr(n -1 + ord('A'))
        
        return self.convertToTitle((n-1)//26) + chr((n-1)% 26 + ord('A'))

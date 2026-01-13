class Solution:
    def completePrime(self, num: int) -> bool:
        """
        1, 3, 5, 7, 9
        """

        s = str(num)
        cands = []
        for i in range(1, len(s)):
            cands.append(int(s[:i]))
        for i in range(len(s)-1, -1, -1):
            cands.append(int(s[i:]))

        if 1 in cands:
            return False
        
        for cand in set(cands):
            if self.prime_factorize(cand) == False:
                return False

        return True

    def prime_factorize(self, num):
        i = 1
        result = []
        while i * i <= num:
            if num % i == 0:
                result.append(i)
                if i * i != num:
                    result.append(num // i)
                if len(result) > 2:
                    return False
            i += 1
        return len(result) <= 2

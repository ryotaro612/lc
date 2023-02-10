class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        i = 1
        total = 0
        while i * i <= num:
            if num % i == 0:
                if i != num:
                    total += i
                if num // i != i and num // i != num:
                    total += num // i
            i += 1
        return num == total

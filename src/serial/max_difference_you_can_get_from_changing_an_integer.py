class Solution:
    def maxDiff(self, num: int) -> int:
        # print(923456 - 113456)
        digits = [ord(c) - ord('0') for c in str(num)]

        n = len(digits)
        
        non_9 = -1
        
        for digit in digits[::-1]:
            if digit != 9:
                non_9 = digit
        
        if non_9 == -1:
            maxi = num
        else:
            maxi = self.convert([9 if non_9 == d else d for d in digits])

        if digits[0] > 1:
            mini = self.convert([1 if d == digits[0] else d for d in digits])
        else:
            non_1 = -1
            for d in digits[::-1]:
                if d > 1:
                    non_1 = d
            
            if non_1 == -1:
                mini = num
            else:
                mini = self.convert([0 if d == non_1 else d for d in digits ])
        
        return abs(maxi - mini)

    
    def convert(self, digits):
        return int(''.join([str(d) for d in digits]))


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            divisors = self.find_divisors(num)
            if len(divisors)  == 4:
                result += sum(divisors)
        
        return result

    
    def find_divisors(self, num):
        result = []
        i = 1
        while i * i <= num:
            if num % i == 0:
                result.append(i)
                if i != num // i:
                    result.append(num // i)
            i += 1
        return result

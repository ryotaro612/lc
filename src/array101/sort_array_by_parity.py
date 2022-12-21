class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for n in nums:
            if n % 2:
                odds.append(n)
            else:
                evens.append(n)
                
        return evens + odds

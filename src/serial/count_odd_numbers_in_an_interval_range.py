class Solution:
    def countOdds(self, low: int, high: int) -> int:

        # 4 8 -> 5, 7 (high - low) // 2
        # 4 9 -> 5 , 7, 9 (high - low) // 2 + 1
        # 5 10 -> 5 7, 9 (high - low) // 2 + 1
        # 3 7 -> 3 5 7 -> (high - low) // 2 + 1

        if high % 2 == 0 and low % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1

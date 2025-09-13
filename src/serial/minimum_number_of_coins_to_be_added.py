class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        """
        maxi = 0

        maxi = 1
        maxi + 1 != coins[i]
        maxi + 1
        result = 0
        
        maxi += coins[i]

        """
        coins.sort()

        result = 0
        maxi = 0
        i = 0
        n = len(coins)
        while maxi < target:

            if i < n:
                if maxi + 1 < coins[i]:
                    result += 1
                    maxi += maxi + 1
                else:
                    maxi += coins[i]
                    i += 1
            else:
                maxi += maxi + 1
                result += 1
        
        return result



"""
[0 0 0 0 0 0] -> 3
[0 0 0 0 0] -> 3
[0 0 0 0] -> 2
[0 0 0] -> 2
[0 0] -> 1
[0] -> 1
n = len(flowerbed)
if n % 2 == 0:
  n // 2
else:
  n // 2 + 1

[0 1] -> 0
[0 0 1] -> 1
[0 0 0 1] -> 1
[0 0 0 0 1] -> 2
[0 0 0 0 0 1] -> 2
[0 0 0 0 0 0 1] -> 3
m = num_of consecutive 0
m // 2

[1 0 1] -> 0
[1 0 0 1] -> 0
[1 0 0 0 1] -> 1
[1 0 0 0 0 1] -> 1
[1 0 0 0 0 0 1] -> 2
[1 0 0 0 0 0 0 1] -> 2
if m % 2 == 0:
  m // 2 - 1
else:
  m // 2
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        n_flowerbed = len(flowerbed)
        left = -1
        result = 0
        for i in range(n_flowerbed):
            if flowerbed[i]:
                if left == -1:
                    num_zeros = i
                    result += num_zeros // 2
                else:
                    num_zeros = i - left - 1
                    if num_zeros % 2 == 0:
                        result += num_zeros // 2 - 1
                    else:
                        result += num_zeros // 2
                left = i
        if left == -1:
            if n_flowerbed % 2 == 0:
                return n <= (n_flowerbed // 2)
            else:
                return n <= (n_flowerbed // 2 + 1)
        else:
            num_zeros = n_flowerbed - 1 - left
            result += num_zeros // 2
            return n <= result

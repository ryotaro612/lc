class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        i = l = 1

        while i * i <= area:
          if area % i == 0:
              l = i
          i += 1

        return [max(l, area //l), min(l, area //l)]

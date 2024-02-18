import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = self._gen(self.x_center)
            y = self._gen(self.y_center)
            if (x-self.x_center)**2 + (y-self.y_center)**2 <= self.radius ** 2:
                return [x, y]
        
    def _gen(self, center):
        return random.uniform(center - self.radius, center + self.radius)        


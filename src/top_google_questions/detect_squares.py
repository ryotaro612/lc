from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0
        for pos_y, num in self.points[x].items():
            if pos_y == y:
                continue
            
            edge = abs(pos_y - y)

            result += self.points[x+edge][y] * self.points[x+edge][pos_y] * num
            result += self.points[x-edge][y] * self.points[x-edge][pos_y] * num
        return result


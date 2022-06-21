"""

"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.snake = [[0, 0]]       
        self.delta = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
        self.food = food
        self.food_index = 0
        
    def move(self, direction: str) -> int:
        head_r, head_c = self.snake[0]
        delta_r, delta_c = self.delta[direction]
        next_head = [head_r+delta_r, head_c + delta_c]
        
        if not self.is_in_screen(next_head):
            return -1
        if next_head == self.get_food_position():
            self.food_index += 1
            self.snake = [next_head] + self.snake
            return self.get_score()
        
        self.snake = [next_head] + self.snake[:-1]
        positions = dict()
        # print(direction, self.food_index, self.snake)
        for r, c in self.snake:
            key = (r, c)
            if key in positions:
                return -1
            positions[key] = True
            
        return self.get_score()
    
    def is_in_screen(self, head):
        return 0 <= head[0] and head[0] < self.height and \
            0 <= head[1] and head[1] < self.width

    def get_food_position(self):
        if self.food_index < len(self.food):
            return self.food[self.food_index]
        return None
    
    def get_score(self):
        return len(self.snake) - 1
    
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

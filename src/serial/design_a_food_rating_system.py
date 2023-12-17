import heapq
from collections import defaultdict
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = dict()
        self.food_cuisine = dict()
        self.cuisine_heap = defaultdict(list)
        n = len(foods)
        for i in range(n):
            self.food_rating[foods[i]] = ratings[i]
            self.food_cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_heap[cuisines[i]], [-ratings[i], foods[i]]) 

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        heap = self.cuisine_heap[self.food_cuisine[food]]
        heapq.heappush(heap, [-newRating, food])
        

    def highestRated(self, cuisine: str) -> str:
        
        heap = self.cuisine_heap[cuisine]
        while True:
            rating, food = heap[0]
            if self.food_rating[food] == -rating:
                return food
            else:
                heapq.heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

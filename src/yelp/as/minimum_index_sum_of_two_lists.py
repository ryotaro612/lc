class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurants = dict()
        for i, restaurant in enumerate(list2):
            restaurants[restaurant] = i
        
        result = []
        
        for i, restaurant in enumerate(list1):
            # result = [(restaunrant, sum)]
            if restaurant in restaurants:
                index_sum = restaurants[restaurant] + i
                if len(result) > 0 and index_sum < result[0][1]:
                    result = []
                if len(result) == 0 or result[0][1] == index_sum:
                    result.append((restaurant, index_sum))
        
        return [t[0] for t in result]

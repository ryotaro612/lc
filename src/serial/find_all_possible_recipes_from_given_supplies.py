from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredients = [set(i) for i in ingredients]
        que = deque(supplies)

        while que:
            #changed = False
            supply = que.popleft()

            for i, ingredient in enumerate(ingredients):
                if supply in ingredient:
                    ingredient.remove(supply)
                    # changed = True
                    if not ingredient:
                        que.append(recipes[i])
                        
            #if not changed:
            #    break
        
        return [r for i, r in enumerate(recipes) if not ingredients[i]]

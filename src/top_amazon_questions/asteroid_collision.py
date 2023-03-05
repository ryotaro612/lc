class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            if stk:
                if asteroid * stk[-1] > 0 or stk[-1] < 0:
                    stk.append(asteroid)
                else:
                    while True:
                        if stk == []:
                            stk.append(asteroid)
                            break
                        elif stk[-1] < 0:
                            stk.append(asteroid)
                            break
                        elif stk[-1] == abs(asteroid):
                            stk.pop()
                            break
                        elif stk[-1] > abs(asteroid):
                            break
                        else:
                            stk.pop()
            else:
                stk.append(asteroid)
        return stk
                    

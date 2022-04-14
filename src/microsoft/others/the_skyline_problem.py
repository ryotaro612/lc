class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:  
        n = len(buildings)
        if n == 0:
            return []
        elif n == 1:
            building = buildings[0]
            return [[building[0], building[2]], [building[1], 0]]
        return self.merge(self.getSkyline(buildings[:n//2]), self.getSkyline(buildings[n//2:]))
    
    def merge(self, left, right):
        left_n = len(left)
        right_n = len(right)
        l = 0
        r = 0
        height = 0
        result = []
        while True:
            if l < left_n:
                if r < right_n:
                    if left[l][0] < right[r][0]:
                        if 0 < r:
                            new_height = max(left[l][1], right[r-1][1]) 
                        else:
                            new_height = left[l][1]
                        if height != new_height:
                            result.append([left[l][0], new_height])
                            height = new_height
                        l += 1
                    elif left[l][0] == right[r][0]:
                        new_height = max(left[l][1], right[r][1])
                        if height != new_height:
                            height = new_height
                            result.append([left[l][0], height])
                        l += 1
                        r += 1
                    else: # right[r][0] < left[l][0]
                        if 0 < l:
                            new_height = max(left[l-1][1], right[r][1]) 
                        else:
                            new_height = right[r][1]
                        if height != new_height:
                            result.append([right[r][0], new_height])
                            height = new_height
                        r += 1
                else:
                    result = result + left[l:]
                    break
            else:
                if r < right_n:
                    result = result + right[r:]
                    break
                else:
                    break
        #print(left, "<->", right, "===> ", result)
        return result

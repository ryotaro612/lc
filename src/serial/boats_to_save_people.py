class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result = 0 
        forward = 0
        backward = len(people) - 1
        while forward <= backward:
            if people[forward] + people[backward] <= limit:    
                forward += 1
                backward -= 1
            else:
                backward -= 1
            result += 1
        return result

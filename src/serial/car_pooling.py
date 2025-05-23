from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        [1, 3, 6]
        d[3] += 1
        d[6] -= 1
        ()
        """
        people = defaultdict(int)
        for n_passengers, start, end in trips:
            people[start] += n_passengers
            people[end] -= n_passengers
        
        change = sorted([[d, n_pass] for d, n_pass in people.items()])

        current = 0
        for d, n_pass in change:
            if current + n_pass > capacity:
                return False
            
            current += n_pass
        
        return True

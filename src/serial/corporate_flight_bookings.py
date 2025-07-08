class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        prefix[first_i-1] += seats_i
        prefix[last_i] -= seats_i
        for 
        prefix[i+1] += prefix[i]
        """
        prefix = [0] * (n + 1)
        for first, last, seats in bookings:
            prefix[first-1] += seats
            prefix[last] -= seats
        
        for i in range(n):
            prefix[i+1] += prefix[i]
        
        return prefix[:-1]

"""
["Uber","startTrip","addCab","addCab","getNearestCabs","startTrip","endTrip","endTrip","getNearestCabs"]
[[],[5,10,15],[10,10],[30,30],[1,12,15],[1,5,5],[5,0,0],[1,0,0],[5,30,30]]
"""
class Uber:

    def __init__(self):
        self.cabs = []        
        self.customers = set()
    def addCab(self, cabX: int, cabY: int) -> None:
        """
        oid addCab(int cabX, int cabY) Adds a cab located at point (cabX, cabY) to the system. Note that multiple cabs can be at the same location.
        """
        self.cabs.append([cabX, cabY])
    def startTrip(self, customerID: int, customerX: int, customerY: int) -> List[int]:
        """
        int[] startTrip(int customerID, int customerX, int customerY) Returns an integer array [nearX, nearY] where nearX and nearY represent the X-coordinate and Y-coordinate (respectively) of the closest available cab to customer customerID, present at (customerX, customerY). In case there are multiple such cabs, it returns the location of the cab with the smallest X-coordinate, and if there are still multiple choices, it chooses the cab with the smallest Y-coordinate. In case there are no available cabs, returns [-1, -1]. The cab is then assigned to the customer, who starts their trip.
        """
        cabs = self.get_nearest_cabs(len(self.cabs), customerX, customerY)
        if cabs:
            cab = cabs[0]
            self.cabs = cabs[1:]
            self.customers.add(customerID)
            return cab
        else:
            return [-1, -1]

    def endTrip(self, customerID: int, customerX: int, customerY: int) -> None:
        """
        void endTrip(int customerID, int customerX, int customerY) The customer customerID ends their trip at (customerX, customerY). In case a cab was assigned to them by the system, re-adds it back to the system at (customerX, customerY), otherwise ignores the call.
        """
        if customerID in self.customers:
            self.customers.remove(customerID)
            self.cabs.append([customerX, customerY])

    def getNearestCabs(self, k: int, x: int, y: int) -> List[List[int]]:
        """
        List<List<Integer>> getNearestCabs(int k, int x, int y) Returns a list of locations of the k closest available cabs to (x, y), sorted in non-decreasing order by X-coordinate and subsequently by Y-coordinate. In case there are multiple choices, it chooses the cab with the smaller X-coordinate, and if there are still multiple choices, it chooses the one with the smaller Y-coordinate. In case there are less than k cabs available, it returns the locations of all of them.
        """
        cabs = self.get_nearest_cabs(k, x, y)
        return sorted(cabs, key=lambda cab: [cab[0], cab[1]])
    def get_nearest_cabs(self, k, x, y):
        return sorted(
            self.cabs,
            key= lambda cab: [(x - cab[0])**2 + (y- cab[1])**2, cab[0], cab[1]]
        )[:k]

# Your Uber object will be instantiated and called as such:
# obj = Uber()
# obj.addCab(cabX,cabY)
# param_2 = obj.startTrip(customerID,customerX,customerY)
# obj.endTrip(customerID,customerX,customerY)
# param_4 = obj.getNearestCabs(k,x,y)

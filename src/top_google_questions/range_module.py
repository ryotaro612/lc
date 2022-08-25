import bisect
"""
["RangeModule","addRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","queryRange"]
[[],[10,180],[150,200],[250,500],[50,100],[180,300],[600,1000],[50,150],[50,100]]

["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]

["RangeModule","addRange","queryRange","addRange","queryRange","addRange","removeRange","removeRange","removeRange","queryRange"]
[[],[5,7],[2,7],[6,9],[2,9],[2,7],[3,10],[1,8],[1,10],[4,7]]

["RangeModule","queryRange","queryRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","addRange","removeRange","addRange","removeRange","removeRange","queryRange","queryRange","queryRange","queryRange","removeRange","addRange","removeRange","queryRange","addRange","addRange","removeRange","queryRange","removeRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange","queryRange","queryRange","addRange","removeRange","addRange","addRange","addRange","queryRange","removeRange","addRange","queryRange","addRange","queryRange","removeRange","removeRange","addRange","addRange","queryRange","queryRange","addRange","addRange","removeRange","removeRange","removeRange","queryRange","removeRange","removeRange","addRange","queryRange","removeRange","addRange","addRange","queryRange","removeRange","queryRange","addRange","addRange","addRange","addRange","addRange","removeRange","removeRange","addRange","queryRange","queryRange","removeRange","removeRange","removeRange","addRange","queryRange","removeRange","queryRange","addRange","removeRange","removeRange","queryRange"]
[[],[21,34],[27,87],[44,53],[69,89],[23,26],[80,84],[11,12],[86,91],[87,94],[34,52],[1,59],[62,96],[34,83],[11,59],[59,79],[1,13],[21,23],[9,61],[17,21],[4,8],[19,25],[71,98],[23,94],[58,95],[12,78],[46,47],[50,70],[84,91],[51,63],[26,64],[38,87],[41,84],[19,21],[18,56],[23,39],[29,95],[79,100],[76,82],[37,55],[30,97],[1,36],[18,96],[45,86],[74,92],[27,78],[31,35],[87,91],[37,84],[26,57],[65,87],[76,91],[37,77],[18,66],[22,97],[2,91],[82,98],[41,46],[6,78],[44,80],[90,94],[37,88],[75,90],[23,37],[18,80],[92,93],[3,80],[68,86],[68,92],[52,91],[43,53],[36,37],[60,74],[4,9],[44,80],[85,93],[56,83],[9,26],[59,64],[16,66],[29,36],[51,96],[56,80],[13,87],[42,72],[6,56],[24,53],[43,71],[36,83],[15,45],[10,48]]

["RangeModule","addRange","removeRange","queryRange","addRange","queryRange","queryRange","removeRange","queryRange","removeRange","queryRange","queryRange","removeRange","addRange","queryRange","addRange","queryRange","queryRange","queryRange","addRange","removeRange"]
[[],[2,4],[1,4],[1,3],[6,10],[2,8],[1,6],[3,7],[1,8],[2,4],[5,6],[6,8],[3,10],[1,6],[5,7],[7,8],[5,10],[7,9],[4,10],[2,6],[2,7]]
"""
class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        if len(self.ranges) == 0:
            self.ranges = [left, right]
            return
        start = bisect.bisect_left(self.ranges, left)
        end = bisect.bisect_right(self.ranges, right)
        if start % 2 == 0:
            if end % 2 == 0:
                self.ranges = self.ranges[:start] + [left, right] + self.ranges[end:]
            else:
                self.ranges[start] = left
                self.ranges = self.ranges[:start+1] + self.ranges[end:]
        else:
            if end % 2 == 0:
                self.ranges[end-1] = right
                self.ranges = self.ranges[:start] + self.ranges[end-1:]
            else:
                self.ranges = self.ranges[:start] + self.ranges[end:]
        # print('add', left, right)
        # print(self.ranges)
        
    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.ranges, left)
        end = bisect.bisect_left(self.ranges, right)
        if end == len(self.ranges):
            return False
        if start % 2 == 0:
            return False
        return start == end
    

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_right(self.ranges, left)
        end = bisect.bisect_left(self.ranges, right)
        
        if start % 2 == 0:
            if end % 2 == 0:
                self.ranges = self.ranges[:start] + self.ranges[end:]
            else:
                if right == self.ranges[end]:
                    #print('hi', start, end)
                    self.ranges = self.ranges[:start] + self.ranges[end+1:]
                else:
                    self.ranges = self.ranges[:start] + [right] + self.ranges[end:]
        else:
            if end % 2 == 0:
                self.ranges = self.ranges[:start] + [left] + self.ranges[end:]
            else:
                self.ranges = self.ranges[:start] + [left, right] + self.ranges[end:]
        # print('remove', left, right)
        # print(self.ranges)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

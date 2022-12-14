from collections import deque
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        result = 0
        que = deque()
        que.append([topRight, bottomLeft])
        while que and result < 10:
            tr, bl = que.popleft()
            if tr.x == bl.x:
                if tr.y == bl.y:
                    if sea.hasShips(tr, bl):
                        # print(tr.x, tr.y)
                        result += 1
                    else:
                        continue
                else:
                    mid = (tr.y + bl.y) // 2
                    if sea.hasShips(Point(tr.x, mid), bl):
                        que.append([Point(tr.x, mid), bl])
                    if sea.hasShips(tr, Point(tr.x, mid+1)):
                        que.append([tr, Point(tr.x, mid+1)])
            else:
                mid = (tr.x + bl.x) // 2
                p0 = Point(mid+1, bl.y)
                p1 = Point(mid, tr.y)
                if sea.hasShips(p1, bl):
                    que.append([p1, bl])
                if sea.hasShips(tr, p0):
                    que.append([tr, p0])
        
        return result

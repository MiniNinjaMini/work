import math
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(f"x={self.x};y={self.y}")
    def move(self,x,y):
        self.x=x
        self.y=y
    def dist(self, other_point):
        print(math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2))

#test
first=Point(5,5)
second=Point(10,10)
second.move(8,9)
first.dist(second) #output 5.0
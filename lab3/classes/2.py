class Shape:
    def __init__(self, length):
        self.length=length
    def area(self):
        print("Area=0")
       
class square(Shape):
    def area(self):
        self.Shapes_area=self.length**2
        print(f"Area={self.Shapes_area}")

#test
romb=Shape(2)
romb.area()
kvadrat=square(2)
kvadrat.area()

#output 0 4
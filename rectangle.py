class Rectangle:
    def __init__(self, l, w):
        self.lenth = l
        self.width = w

    def rectangle_area(self):
        return self.lenth * self.width

newRectangle = Rectangle(777,777)
print("dimension of a Rectangle - Length : %d width : %d" % (newRectangle.lenth, newRectangle.width))
print("area of a Rectangle :", newRectangle.rectangle_area())
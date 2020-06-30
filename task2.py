# 2. Define a class named Shape and its subclass Square. The Square class has an 
# init function which takes a length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape():
    def __init__(self,length):
        self.length=length
    def area(self,length):
        return 0

class Square(Shape):
        def __init__(self,length):
            self.length=length
        def area(self,length):
            return self.length*self.length
sh=Shape(10)
print (sh.area(10))
s=Square(sh)
s.length=20
print(s.area(s.length))
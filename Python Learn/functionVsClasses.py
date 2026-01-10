# function to calculate area of rectangel
def calculate_rectangle_area(length,width):
    return length*width

print(calculate_rectangle_area(5,10))


###CLASS###

class Rectangle:
    
    ##__init__ is a constructor, runs automatically when you create a new object from a class
    def __init__(self, length,width):
        self.length=length
        self.width=width
    #self refferes to the current object of the class and lets it sore and use its own data
    def calculate_area(self):
        return self.length*self.width
    

myRectangle=Rectangle(6,12)
print(myRectangle.calculate_area())
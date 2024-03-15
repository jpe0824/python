from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def setLocation(self):
        pass

    @abstractmethod
    def getLocation(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def fill(self):
        pass

    @abstractmethod
    def setColor(self):
        pass

    @abstractmethod
    def undisplay(self):
        pass
class Point(Shape):
    def setLocation(self):
        print("Setting location for Point")

    def getLocation(self):
        print("Getting location for Point")

    def display(self):
        print("Displaying Point")

    def fill(self):
        print("Filling Point")

    def setColor(self):
        print("Setting color for Point")

    def undisplay(self):
        print("Undisplaying Point")
class Line(Shape):
    def setLocation(self):
        print("Setting location for Line")

    def getLocation(self):
        print("Getting location for Line")

    def display(self):
        print("Displaying Line")

    def fill(self):
        print("Filling Line")

    def setColor(self):
        print("Setting color for Line")

    def undisplay(self):
        print("Undisplaying Line")
class Rectangle(Shape):
    def setLocation(self):
        print("Setting location for Rectangle")

    def getLocation(self):
        print("Getting location for Rectangle")

    def display(self):
        print("Displaying Rectangle")

    def fill(self):
        print("Filling Rectangle")

    def setColor(self):
        print("Setting color for Rectangle")

    def undisplay(self):
        print("Undisplaying Rectangle")
class CircleAdapter(Shape):
    def __init__(self, circle) -> None:
        self.circle = circle

    def setLocation(self):
        self.circle.setLocation()

    def getLocation(self):
        self.circle.getLocation()

    def display(self):
        self.circle.displayIt()

    def fill(self):
        self.circle.fillIt()

    def setColor(self):
        self.circle.setItsColor()

    def undisplay(self):
        self.circle.undisplayIt()
class XXCircle():
    def setLocation(self):
        print("Setting location for Circle")

    def getLocation(self):
        print("Getting location for Circle")

    def displayIt(self):
        print("Displaying Circle")

    def fillIt(self):
        print("Filling Circle")

    def setItsColor(self):
        print("Setting color for Circle")

    def undisplayIt(self):
        print("Undisplaying Circle")

def main():
    point = Point()
    line = Line()
    rectangle = Rectangle()
    circle = CircleAdapter(XXCircle())

    point.setLocation()
    point.getLocation()
    point.display()
    point.fill()
    point.setColor()
    point.undisplay()

    line.setLocation()
    line.getLocation()
    line.display()
    line.fill()
    line.setColor()
    line.undisplay()

    rectangle.setLocation()
    rectangle.getLocation()
    rectangle.display()
    rectangle.fill()
    rectangle.setColor()
    rectangle.undisplay()

    circle.setLocation()
    circle.getLocation()
    circle.display()
    circle.fill()
    circle.setColor()
    circle.undisplay()

if __name__ == "__main__":
    main()
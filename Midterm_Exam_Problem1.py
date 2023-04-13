class Circle:
    def __init__(self, measuremet):
        self.measurement = measuremet

        if measuremet <= 0:
            print("The measurement must be a positive number")
        self.radius = measuremet / 2 if measuremet <= 1000 else None
        if self.radius is None:
            print("Error")

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * self.radius

if __name__ == '__main__':
        diameter = float(input("Enter the diamter: "))
        radius = float(input("Enter the radius: "))
        circle = Circle(diameter)
        print("The area of the circle is " , circle.area())
        print("The perimeter of the circle is ", circle.perimeter())




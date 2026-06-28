"""
Polygon Area Calculator

Models rectangles and squares using object-oriented programming.
Completed as part of the freeCodeCamp Scientific Computing with Python certification.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""

        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Rectangle")
    print(rect)
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")
    print(f"Diagonal: {rect.get_diagonal():.2f}")
    print(rect.get_picture())

    square = Square(4)
    print("Square")
    print(square)
    print(f"Area: {square.get_area()}")
    print(f"Perimeter: {square.get_perimeter()}")
    print(f"Diagonal: {square.get_diagonal():.2f}")
    print(square.get_picture())

    rect.set_width(16)
    rect.set_height(8)
    print(f"Squares inside rectangle: {rect.get_amount_inside(square)}")

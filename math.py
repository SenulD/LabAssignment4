def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

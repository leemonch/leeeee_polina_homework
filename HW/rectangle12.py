class Rectangle:
    def __init__(self, corner1, corner2):
        self.left = min(corner1[0], corner2[0])
        self.top = max(corner1[1], corner2[1])
        self.right = max(corner1[0], corner2[0])
        self.bottom = min(corner1[1], corner2[1])

        self.width = self.right - self.left
        self.height = self.top - self.bottom

    def get_pos(self):
        return (round(self.left, 2), round(self.top, 2))

    def get_size(self):
        w = round(self.right - self.left, 2)
        q = round(self.top - self.bottom, 2)
        return (w, q)

    def perimeter(self):
        result = 2 * (self.width + self.height)
        return round(result, 2)

    def area(self):
        result = self.width * self.height
        return round(result, 2)

    def move(self, dx, dy):
        self.left += dx
        self.right += dx
        self.top += dy
        self.bottom += dy

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.right = self.left + self.width
        self.bottom = self.top - self.height


import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    # sumPoints
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # distanceBtn Points
    def distance_btn_points(self, other):
        x_diff = other.x - self.x
        y_diff = other.y - self.y
        return math.sqrt(math.pow(x_diff, 2) + math.pow(y_diff, 2))

        # midPoint
    def mid_point(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)
        # translatePoint


point = Point(1, 2)
other = Point(3, 4)

print(point + other)
dist = point.distance_btn_points(other)
print(format(dist, '.2f'))

mid = point.mid_point(other)
print(mid)

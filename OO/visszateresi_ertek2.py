# féltáv
def halfway(one_point, other_point):
    mx = (one_point.x + other_point.x) / 2
    my = (one_point.y + other_point.y) / 2
    return Point(mx, my)

class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    # origótól való távolság
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(5, 12)
q = Point(22, 44)
print(halfway(p, q))

# most viszont egy saját az osztályon kívüli függvény
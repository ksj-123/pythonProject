
class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    # origótól való távolság
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # saját típus kiíratás
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(5, 12)
q = Point(22,44)
print(p, q)
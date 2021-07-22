# saját típusból érték visszaadás
class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    # origótól való távolság
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5



p = Point(5, 12)
print(p.distance_from_origin())
q = Point()
print(q.distance_from_origin())
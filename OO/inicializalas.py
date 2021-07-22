#
class Point:
    def __init__(self, _x=1, _y=2):
        self.x = _x
        self.y = _y


# osztály példányosítása ahol meg kell adnom a paramétereket!
p = Point(5, 12)
print(p.x, p.y)
# ha nem adok meg értéket, akkor azt fentről veszi
q = Point()
print(q.x, q.y)
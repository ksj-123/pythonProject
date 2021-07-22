class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    # belső függvény az objektumon belül
    def print_p(self):
        print(self.x, self.y)

    def print_p_2(self):
        self.print_p()

p = Point()
p.print_p()

class MessageBox():
    def __init__(self):
        self.x = 1
        self.y = 2

        def distance_from_origin(self):
            return ((self.x ** 2) + (self.y ** 2)) ** 0.5

operations = [1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1]

mb = MessageBox()
mb.send()
mb.send()
mb.receive()
mb.receive()
mb.send()

print(mb.operations())

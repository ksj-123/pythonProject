# random generálja a felhasználó nevet, jelszót, emailt

import random
import string


# abcdefghijklmnoprstq...
# random.randint(a,b) --> 1,55,22,...
# username (min8, max16), password, email
# random.choice(string.ascii_lowercase)
class MyRND():
    chars = string.ascii_lowercase
    pchars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

    @classmethod
    def uname(cls):
        return "".join([random.choice(cls.chars) for _ in range(8)])

    @classmethod
    def ppass(cls):
        return "".join([random.choice(cls.pchars) for _ in range(8)])

    @classmethod
    def email(cls):
        # 1. generalom a random kukac elotti reszt
        # @
        # 2. generalom a kukac utanni reszt
        # .
        # fixen "com"
        pass


print(MyRND.uname())
print(MyRND.ppass())


class TestData:
    def __init__(self):
        self.data = []
        for i in range(99):
            d = {}
            d["username"] = MyRND.uname()
            d["password"] = MyRND.ppass()
            self.data.append(d)


td = TestData()
print(td.data)
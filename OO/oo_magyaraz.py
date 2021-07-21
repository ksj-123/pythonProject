# 3         --> int     => int()
# "Tamas"   --> str     => str()
# 3.14      --> float   => float()
# True      --> bool    => bool()
# class int:
#     def __init__(self, value):
#         self.value = value
# tervrajzt az a osztály (class)
# epulet az a példány (instance, object)
class NameTestData:
    def __init__(self, firt_name, quantity=0, last_name=""):
        self.firt_name = firt_name
        self.quantity = quantity
        self.last_name = last_name
        # self.full_name = f"{self.firt_name} {self.last_name}"
    def __str__(self):
        return f"*NameTestData({self.firt_name}, {self.quantity})"
    def __repr__(self):
        return f"!NameTestData({self.firt_name}, {self.quantity})"
    def full_name(self):
        return f"{self.firt_name} {self.last_name}"

nj = NameTestData("Janos", 11, "Nagy")
print(nj)
test_data = [NameTestData("Tamas", 15, "Jozsa"), NameTestData("Gabor"), NameTestData("Nora")]
print(test_data)
for data in test_data:
    print(data.full_name())

# Rossz megoldas
# name = "Tamas"
# name2 = "Gabor"
# name3 = "Nora"
# Nem annyira rossz megodas
# names = ["Tamas", "Gabor", "Nora"]
# neg_names = [0, None, ""]
# Jo megoldas
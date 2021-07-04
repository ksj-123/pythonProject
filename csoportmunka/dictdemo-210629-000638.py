# lista

lista1 = [1, 5, 3, 7, 2, 3, 4, 5]  # sorrend fontos
print(lista1)
lista1.append(4)
print(lista1)
lista1.pop()
print(lista1)
l = []

print('0->', lista1[0])
print('1->', lista1[1])
# l = [l1,l2,l3....]

# tuple, constans lista, verktor, ...

t = (1, 4, 6, 3, 2, 43, 4)  # sorrend fontos, és, hogy konstans
t1 = ((1, 2), (2, 3), (5, 6))
print('0,1->', t1[0][1])

print(t)
tmp_list = list(t)
print(tmp_list)
tmp_list.append(111)
print(tmp_list)
t = tuple(tmp_list)
print(t)

# dict
# kulcs/index csak olyan tipus lehet ami HASH-elheto
d = {}
d = {"nev": "Tamas",
     "kor": "kerekderek",
     "address": {"irsz": 2143}
     }

print(d["nev"])
print(d["address"]["irsz"])

d["allatbarat"] = True

print(d)

# set ---> csak egyedi ertekeket tarolunk
s = set()
s = {2, 5, 6, 7, 5, 5, 5, 5, 5, 5}
print(s)
lista1 = [1, 5, 3, 7, 2, 3, 4, 5]
print(lista1)
lista1 = list(set(lista1))
print(lista1)
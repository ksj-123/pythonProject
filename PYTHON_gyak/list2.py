my_list = [1, 2, 3, 4.5, "alma", True]
print(len(my_list))

my_nested_list = [1, 2, [1, 2], "alma"]

####

my_list = [1, 2, 3, 4, "alma"]

print(my_list[0])
# ez a 0. elem, vagyis az 1

print(my_list[-1])
# ez a lista hátulról a 0. eleme, vagyis az "alma"

####
my_list = [1, 2, 3, 4.5, "alma"]

my_len = len(my_list)
print(my_len)

it_length = int(input())
my_list = []
for i in range(it_length):
    my_list.append(i)

print(len(my_list))

####
fruits = ["alma", "körte", "banán"]

print("citrom" in fruits) #igaz e hogy a citrom benne van e a listában
print("alma" in fruits)


my_fruit = input()
print(my_fruit in fruits)


####
# lista fűzés

a = [1, 2, 3]
b = [5, 6]

c = a + b
print(c)

# lista szorzás

a = [1, 2, 3]
b = [5, 6]

c = a * 3
print(c)

####
# lista elem módosítása
my_list = [1, 2, 3]
print(my_list)
my_list[0] = "alma"    # a my_list 1. elemét átírjuk "alma"-ra, de bővíteni nem lehet a listát, tehát nem tehetünk hozzá 4. elemet
print(my_list)

#####
# lista vágása

my_list = [1, 2, 3, "alma", "korte", 3.14]

my_sliced_list = my_list[0:2]    # azt fogjuk elérni, hogy az 1. és 2. elemek lesznek felsorolva a továbbiakban, kivágjuk (felül nyitott)
print(my_list)
print(my_sliced_list)

# [:2] ez azt jelenti, mint az előbb, hogy az 1. és 2. elemek lesznek kivágva az új listába
# [2:] ez pedig azt jelenti, hogy a 3. lemtől lesznek felsorolva, kivágva az új listába
# [:] a teljes listát kivágja (tulajdonképpen lemásolja)

####
# lista elem törlése

my_list = [1, 2, 3, "alma", "korte", 3.14]
print(my_list)
del my_list[3]      # kitörlésre kerül a 3. elem, az pedig az "alma" (mindig 0. az első elem
print(my_list)











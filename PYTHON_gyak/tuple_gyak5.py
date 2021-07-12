# 1) írj egy Python programot ami bekér intput() fügvénnyel egy vesszővel elválasztott számsorozatot és generál a számokból egy listát és egy tuple-t.
# Mind a lista, mind a tuple, tartalmazza az összes számot, ugyan olyan sorrendben, mint ahogy beolvastuk őket.
# Pl: Ha ezt a számsort olvastuk be
#    34,67,55,33,12,98
# akkor annek ez kell legyen a kimenete
#   ['34', '67', '55', '33', '12', '98']
#    ('34', '67', '55', '33', '12', '98')

# További tippek:
# - nem kell a bemeneti hibákat kezelni
# - nem kell javítani ha eseleg nem elfogadható karaktereket ad be a felhasználó
# - a tuple() beépített függvény tud listát konvertálni

my_list = []
my_tuple = ()

def beker():
    adat = input("Kérek egy számsort: ")
    my_list.append(adat)
    print(my_list)

beker()

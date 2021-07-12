# 1) Adott számokat tartalmazó lista.
# Pl. [11, 45, 8, 11, 23, 45, 23, 45, 89]
#
# Írj egy olyan Python programot ami egy asszociatív tömbben eltárolja a lista elemeinek előfordulási számát.
#
# A fenti példára a kimenet: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}


list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

dict_1 = {}

for i in list:
    dict_1[i] = list.count(i)
print(dict_1)

#----------

l = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d = {x: l.count(x) for x in l}
print(d)

#-------

lista_1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

asszoc_tomb = {}

halmaz = set(lista_1)

for elem in halmaz:
    asszoc_tomb[elem] = lista_1.count(elem)

print(asszoc_tomb)
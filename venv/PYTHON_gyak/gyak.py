##### x = ord("a")
##### print(x)

##### x = chr(97)
##### print(x)

##### x = 0


for i in range(97,124,1):
    print(i, chr(i))

for i in range(26):
    szam = i + 97
    print(szam)

for i in range(26):
    szam = i + 97
    print(szam, chr(szam))

# megoldás for ciklussal
for i in range(26):
    szam = i + 97
    print(szam)
    if szam > 122:
        break
# ha szeretnéd listába rendezni, és onnan kiírni:
szamsor = range(200)
szakasz = list(szamsor[97:123])
print(szakasz)
for i in szakasz:
    print(i)
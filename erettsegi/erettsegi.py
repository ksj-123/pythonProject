"""Gödrök érettségi feladat, 2021. május 17."""


def f(i):
    print(f'\n{i}. feladat')


f(1)
with open('melyseg.txt') as bemenet:
    melysegek = [int(line) for line in bemenet]
darab = len(melysegek)
print(f'A fájl adatainak száma: {darab}.')

f(2)
hely = int(input('Adjon meg egy távolságértéket! '))
print(f'Ezen a helyen a felszín {melysegek[hely - 1]} méter mélyen van.')

f(3)
print(f'Az érintetlen terület aránya {melysegek.count(0) * 100 / darab:.2f}%.')

# A 4. feladat regexekkel egyszerűbb lehet, de szándékosan a tananyag keretei
# között maradok inkább.
godrok_temp = ' '.join([str(n) for n in melysegek]).split(' 0')
godrok = []
for s in godrok_temp:
    if s:
        godrok.append(s)
if godrok[0] == '0':
    godrok = godrok[1:]
with open('godrok.txt', 'w') as kimenet:
    for i in range(len(godrok)):
        kimenet.write(''.join(list(godrok[i])).strip() + '\n')

f(5)
print(f'A gödrök száma: {len(godrok)}.')

f(6)
if melysegek[hely - 1] == 0:
    print('Az adott helyen nincs gödör.')
else:
    kezd = hely - 1
    while melysegek[kezd] > 0:
        kezd -= 1
    vege = hely - 1
    while melysegek[vege] > 0:
        vege += 1
    print(f'a)\nA gödör kezdete: {kezd + 2} méter, a gödör vége: {vege} méter.')

    # A b) nem kellemes feladat. Rendeljünk a párokhoz előjelet!
    # Ha a sorrozatban első +1-től jobbra van -1, akkor nem mélyül.
    godor = melysegek[kezd + 1:vege]
    sgn = []  # Sajnos nincs beépített sgn függvény.
    for i in range(1, len(godor)):
        if godor[i] > godor[i - 1]:
            sgn.append(-1)
        elif godor[i] < godor[i - 1]:
            sgn.append(1)
        else:
            sgn.append(0)
    try:
        elsonovekedes = sgn.index(1)
        try:
            utanacsokkenes = sgn[elsonovekedes:].index(-1)
            melyul = False  # Megtaláltuk a növekedés után a csökkenést.
        except ValueError:  # Nem találtuk.
            if -1 in sgn[:elsonovekedes]:
                melyul = True
            else:
                melyul = False  # Végig monoton nő.
    except ValueError:
        melyul = False  # Sehol nem volt növekedés, végig mélyül.
    if len(godor) == 1:
        melyul = True  # Elfajult eset, külön kell rendelkezni róla.
    print('b)')
    if melyul:
        print('Folyamatosan mélyül.')
    else:
        print('Nem mélyül folyamatosan.')

    print(f'c)\nA legnagyobb mélysége {max(godor)} méter.')
    print(f'd)\nA térfogata {10 * sum(godor)} m^3.')
    print(f'e)\nA vízmennyiség {10 * (sum(godor) - len(godor))} m^3.')

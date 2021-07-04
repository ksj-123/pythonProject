# and or not
x = 5
y = -3

if x < 0 and y < 0:
    print('mindkettő negatív')

if x < 0 or y < 0:
    print('van köztük negatív')

if not x <= 0:
    print('x pozitív')

# eljárás / függvény
    # Eljárás definíciója
    def koszont_nevvel(nev):
        print('Szia ' + nev + ', üdv a fedélzeten!')


    # Eljárás hívása
    koszont_nevvel('Ádám')

    # Függvény definíciója
    def festek_kalkulator(x, y):
        '''
        Kiszámolja az adott falfelület festéséhez
        szükséges festék mennyiségét
        '''
        t = x * y
        l = t * 0.13
        return l


    # Függvény hívása
    liter = festek_kalkulator(5, 2)

    # A függvény hívása lehet egy kifejezés része is
    ar = festek_kalkulator(5, 2) * 700

# if - elif - else

  szam = int(input('Adj meg egy számot! '))
  if szam < 0:
      print('A megadott szám negatív.')
  elif szam == 0:
      print('A megadott szám nulla.')
  else:
      print('A megadott szám negatív.')
  print('>> A program vége! <<')

# listák bejárása

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
    print(tantargy)

honapok = ['január', 'február', 'március', 'április', 'május', 'június']

for index, honap in enumerate(honapok):
    print(index, honap)

# listaelemek leképezése

    eredeti = [11, 19, 7, -3]
    eredmeny = [x * 2 for x in eredeti]
    eredmeny_szurve = [x * 2 for x in eredeti if x > 0]

# random
'''
  A random modul randint() metódusa 
  a megadott intervallumon belüli véletlen egész számmal tér vissza.
  '''
import random

random_szam = random.randint(1, 10)
print(random_szam)

'''
A random modul choice() metódusa 
a szekvencia (itt lsita) egy véletlenszerűen megadott elemével tér vissza.
'''
import random

gyumolcsok = ['alma', 'körte', 'eper', 'banán', 'szőlő']
print("A választott gyümölcs: ", random.choice(gyumolcsok))

szamok = [17, 19, 21, 11, 18]
print("A választott szám: ", random.choice(szamok))

# range
# 0 -> 9
for i in range(10):
    print(i)

# while
    # while magyarul azt jelenti: amíg
    # 1 -> 10

    szam = 1
    while szam <= 10:
        print(szam)
        szam = szam + 1

# while
folytatja = True
  while folytatja:
      print('Vidd ki a szemetet!')
      valasz = input('Mondjam még egyszer? (i/n)')
      if valasz == 'n':
          folytatja = False
  print('>> Program vége! <<')

# while break-kel (megállítja a ciklust)
szamlalo = 1
while szamlalo < 100:
    print(szamlalo)
    if (szamlalo % 13 == 0):
        break  # megszakítja a ciklust
    szamlalo = szamlalo + 1

# Mivel az input függvény mindig sztringet ad vissza,
# ha számot kérsz be, ne feledkezz meg a típusátalakításról!
szam = int(input('Adj meg egy számot! '))

# Típusok konvertálása a lista () és a tuple () függvényekkel
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']

# if - elif - else szerkezet
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print('A megadott szám negatív.')
elif szam == 0:
    print('A megadott szám nulla.')
else:
    print('A megadott szám pozitív.')
print('>> A program vége! <<')







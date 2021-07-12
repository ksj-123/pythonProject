# 2) írj egy Python programot ami bekér intput() függvénnyel egy mondatot és megszámolja, hogy hány nagy - és hány
# kisbetű volt a mondatban. Pl: erre a bemenetre
# Hello world!
# ez kell legyen a kimenet
# UPPER CASE 1
# LOWER CASE 9
# További tippek:
# - a charakter pythonban egy egybetűs str típusú változó / érték
# - az str egy karakter lánc tehát lehet rajta iterálni
# - nem kell javítani ha eseleg nem elfogadható karaktereket ad be a felhasználó
# - az str típusnak vannak olyan metódusai amikkel el lehet dönteni, hogy csak kisbetű, vagy nagybetű van - e benne

my_input = input("Kérek egy mondatot!")
my_input = newsample.lower()
for item in set(my_input):
      print(my_input.count(item))


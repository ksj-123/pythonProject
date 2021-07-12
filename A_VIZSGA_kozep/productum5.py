# Nevezzük speciálisnak azokat a számokat, amik `11` többszörösei (másként fogalmazva oszthatók `11`-el) vagy
# pont `1`-el nagyobbak mint `11` valamelyik többszöröse (másként fogalmazva `x-1` már osztható `11`-el).
# írj egy olyan Python függvényt, ami megkapja a tesztelt számot paraméterként és visszaadja,
# hogy a kérdéses szám az speciális vagy nem:

# ```Python
# special_eleven(22) -> True
# special_eleven(23) -> True
# special_eleven(24) -> False
# ```

# Próbáld ki a függvényed az alábbi számokra:
# ```
# 23, 24, 122, 96
# ```

def special_eleven(number):
    if number % 11 == 0:
        return True
    elif number % 11 == 1:
        return True
    else:
        return False


def main_eleven():
    print(23, special_eleven(23))
    print(24, special_eleven(24))
    print(122, special_eleven(122))
    print(96, special_eleven(96))


main_eleven()

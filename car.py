# Egy autokereskedes honlapjan vagyunk. Krealjunk egy menut, az alabbi menupontokkal:
# 1, Kocsi felvetel.  Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi.
# 2, Osszes kocsi adatai lekerdezese
# 3, Kocsi adatainak lekerdezese index alapjan. (marka, eletkora)
# 4, Kocsi eladasa
# 5, Kilepes az applicaciobol

def print_menu():
    # itt kódold a menü kiiratást
    pass

print("1, Kocsi felvetel.  Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi.", "2, Osszes kocsi adatai lekerdezese", "3, Kocsi adatainak lekerdezese index alapjan. (marka, eletkora)", "4, Kocsi eladasa", "5, Kilepes az applicaciobol")

def ask_user_input_for_menu():
    # itt kodold le az adatbekérést
    pass

marka = input("Milyen márkájú kocsi?")
print(marka)
age = int(input("Hány éves a kocsi?"))
print(age)

def register_car():
    # itt kodold le az auto regisztraciojat / adatbekereset / menteset a memoriaban valamilyen kontener tipusu valtozo
    # vagy valtozokba, miert ne lehetne tobb is az egyszeruseg kedveert
    pass



def cars_details():
    # ide kodold le a memoriaban levo osszes kocsi kinyomtatasat a konzolra
    pass

my_list

def car_details_by_id(car_index):
    # ide kodold le annak az egy darab kocsi adatainak kiiratasat ami az adott car_index index alatt van tarolva a
    # valtozo(k)-ban
    pass

my_list

def car_sell(car_index):
    # ide kodol le az auto eladasat / torleset a memoriaban levo tarolobol
    pass

my_list del

def start_application():
    # a menukezelest megirtam neked
    print("Welcome to PM car dealership!")
    print_menu()
    running = True
    while running:
        user_pick = int(ask_user_input_for_menu())
        if user_pick == 1:
            register_car()
        elif user_pick == 2:
            cars_details()
        elif user_pick == 3:
            car_index = int(input("Which car you wanna check?: "))
            car_details_by_id(car_index)
        elif user_pick == 4:
            car_index = int(input("Which car you wanna sell?: "))
            car_sell(car_index)
        else:
            running = False
            print("Thank you. Have a nice day.")

# esetlegesen ide vegyel fel global valtozot(kat) amibe(kben) tarolod az auto adatait
start_application()
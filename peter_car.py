# Egy autokereskedes honlapjan vagyunk. Krealjunk egy menut, az alabbi menupontokkal:
# 1, Kocsi felvetel.  Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi.
# 2, Osszes kocsi adatai lekerdezese
# 3, Kocsi adatainak lekerdezese index alapjan. (marka, eletkora)
# 4, Kocsi eladasa
# 5, Kilepes az applicaciobol

cars_datas = []

def print_menu():
    # itt kódold a menü kiiratást
    print('')
    print('* * * * * MENÜ * * * * *')
    print('1. Kocsi felvétel')
    print('2. Összes kocsi adatainak lekérdezése')
    print('3. Kocsi adatainak lekérdezése index alapján')
    print('4. Kocsi eladása')
    print('5. kilépés')
    print('')


def ask_user_input_for_menu(question):
    # itt kodold le az adatbekérést
    return input(question)


def register_car():
    # itt kodold le az auto regisztraciojat / adatbekereset / menteset a memoriaban valamilyen kontener tipusu valtozo
    # vagy valtozokba, miert ne lehetne tobb is az egyszeruseg kedveert
    car_type = ask_user_input_for_menu('Adja meg az autó típusát: ')
    car_age = ask_user_input_for_menu('Adja meg az autó korát: ')
    car_data = {}
    car_data["brand"] = car_type
    car_data["age"] = int(car_age)
    cars_datas.append(car_data)


def cars_details():
    if len(cars_datas) == 0:
        print('Nincs adat az adatbázisban!')
    else:
        for car in cars_datas:
            print(f'Típus: {car["brand"]}; Kor: {car["age"]}')


def car_details_by_id(car_index):
    # ide kodold le annak az egy darab kocsi adatainak kiiratasat ami az adott car_index index alatt van tarolva a
    # valtozo(k)-ban
    print(f'Típus: {cars_datas[car_index]["brand"]}; Kor: {cars_datas[car_index]["age"]}')


def car_sell(car_index):
    # ide kodol le az auto eladasat / torleset a memoriaban levo tarolobol
    print(f'Típus: {cars_datas[car_index]["brand"]}; Kor: {cars_datas[car_index]["age"]} jármű eladva')
    cars_datas.pop(car_index)


def start_application():
    # a menukezelest megirtam neked
    print("Welcome to PM car dealership!")
    running = True
    while running:
        print_menu()
        user_pick = int(ask_user_input_for_menu('Válassz egy menüpontot [1-5]: '))
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
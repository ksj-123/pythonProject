with open("t_adat.txt", 'r') as data:
    with open("t_masik.txt", 'w') as out:
        out.write(data.read())
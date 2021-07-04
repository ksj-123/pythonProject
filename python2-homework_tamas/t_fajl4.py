with open("t_adat.txt", 'r') as data:
    with open("t_masik.txt", 'w') as out:
        lines = data.readlines()
        for line in lines:
            out.write(line)
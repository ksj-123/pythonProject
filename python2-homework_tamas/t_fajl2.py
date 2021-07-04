with open("t_adat.txt", 'r') as data:
    lines = data.readlines()
    for line in lines:
        if lines.index(line) != len(lines)-1:
            print(line[:-1], end=' ')
        else:
            print(line)
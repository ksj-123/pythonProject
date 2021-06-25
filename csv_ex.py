import csv

with open("data.csv") as file:
    # reader = csv.reader(file)
    # next(reader)
    # for data in reader:
    #     print(data)
    lines = file.readlines()
    for line in lines[1:]:
        print(line.replace("\n", "").split(','))
numbers = [1, 2, 3, 5, 7]
stringek = [str(i) for i in numbers]
for i in [1]:
    print(numbers, " => ", " * ".join(stringek), " = ",
          numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4])

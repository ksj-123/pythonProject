with open("input.txt", "w") as file:    # az input.txt fájlba kiírjuk hogy "alma"
    file.write("alma")

with open("input.txt", "r") as file2:   # visszaolvassa az input.txt fáljból az "alma" szót és beáírja a terminálba
    result = file2.read()
    print(result)

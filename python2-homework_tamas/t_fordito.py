li = []

print("kérem a számokat (kilépés 0)")
while True:
    i = int(input())
    if i == 0:
        break
    else:
        li.append(i)
print(li[::-1])

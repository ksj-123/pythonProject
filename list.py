l = [1, 2, 3, 4, 5]

for i in l:
    if l.index(i) > 2:
        break
    print(i)

for i in l[:3]:
    print(i)
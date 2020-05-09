rows = int(input("masukan rows ")) + 1
for row in range(1, rows):
    nom = 2
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print(nom, end=' ')
            nom += 2
    print("")

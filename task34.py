sonlar = []
for i in range(6):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

juftliklar = []
for i in range(len(sonlar)):
    for j in range(i + 1, len(sonlar)):
        if sonlar[i] + sonlar[j] == 10:
            juftliklar.append((sonlar[i], sonlar[j]))

print("Yig'indisi 10 bolgan juftliklar:", juftliklar)
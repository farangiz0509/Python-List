sonlar = []
kop = 1
for i in range(10):
    son = int(input(f"{i + 1} sonni kiriting : "))
    sonlar.append(son)

kop_takrorlangan = []
for son in sonlar :
    if sonlar.count(son) > kop: 
        kop_takrorlangan.append(son)

print(" kop Takrorlangan sonlar ",kop_takrorlangan)
sozlar = []
necha_martta = int(input("nechta soz kiritasz  :"))

for i in range(necha_martta):
    soz = input(f"{i+1} - sozni kiriting : ").lower()
    sozlar.append(soz)

palidromlar = []

for soz in sozlar:
    if soz == soz[::-1]:
        palidromlar.append(soz)

print("Bu yerda bor palidrom sozlar ",palidromlar)
sozlar = input("Sozlar royxatini vergul bilan ajratib kiriting: ").split(",")

uzun_sozlar = []
for soz in sozlar:
    soz = soz.strip()  
    if len(soz) > 5:
        uzun_sozlar.append(soz)

# Natija
print("Uzunligi 5 dan katta bolgan sozlar:", uzun_sozlar)
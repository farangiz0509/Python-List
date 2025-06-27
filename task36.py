sozlar = input("Sozlar royxatini vergul bilan kiriting: ").split(",")
sozlar = [s.strip() for s in sozlar]

eng_uzun = max(sozlar, key=len)
print("Eng uzun soz:", eng_uzun)
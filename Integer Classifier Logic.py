sayilar = [0, -2, 7, 10, 15]

for x in sayilar:
    if x == 0:
        print(f"{x} sayısı etkisiz eleman (sıfır).")
    elif x % 2 == 0:
        print(f"{x} sayısı çift bir sayıdır.")
    else:
        print(f"{x} sayısı tek bir sayıdır.")

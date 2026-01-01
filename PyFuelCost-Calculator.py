benzin_fiyati= 50.36
dizel_fiyati= 42.80
lpg_Fiyati= 30.30

ortalamaYakitTületimi = float(input("100 km deki ortalama yakıt tüketimi : "))
gidilecekyol = float(input(" gidelen mesafe : "))
yakitTipi = input("yakıt tipi : ")
toplamYakitTüketimi = gidilecekyol * (ortalamaYakitTületimi) / 100

if(yakitTipi=="benzin") :
    toplamYakitTüketimi= benzin_fiyati* toplamYakitTüketimi
    print(toplamYakitTüketimi)
elif (yakitTipi == "dizel") :
    toplamYakitTüketimi= dizel_fiyati* toplamYakitTüketimi
    print(toplamYakitTüketimi)
elif ( yakitTipi == "lpg") :
    toplamYakitTüketimi = lpg_Fiyati* toplamYakitTüketimi
    print(toplamYakitTüketimi)
else :
    print("yalnıs yakit")

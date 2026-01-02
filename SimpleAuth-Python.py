dogru_sifre="python123" 
hak = 3

while hak >0:
    sifre=input("şifreyi giriniz: ")
    if sifre=="":
        print("boş geçemezsiniz")
        continue
    if sifre == dogru_sifre:
        print("giriş başarılı ")
        break
    hak-=1
    print("hatalı şifre hakkınız: ", hak)
else:
    print("hesap kitlendi")

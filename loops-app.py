import random
sayi = random.randint(1,10)
can = int(input("kaç can kullanmak istersiniz"))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmininiz: "))

    if tahmin == sayi:
         print(f"tebrikler {sayac}. da/de doğru tahmin.Toplam puanınız: {100 - (100/can) * (sayac-1)}")
         break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşşağı")
    if hak == 0:
        print(f"hakkınız bitti.Tutulan sayi {sayi}")  

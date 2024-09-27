import math

tekrarEtmeyenSayi = [1,2,3,4,5]
tekrarEdenSayi = [1,1,3,4,5]

kontrolSayisi = 0

def tekrarKontrol(liste):
    gorulenSayilar = []

    for i in range(len(liste)):
        kontrolSayisi = liste[i]

        if kontrolSayisi in gorulenSayilar:
            print("Tekrar eden sayı var.")
            return
        else:
            gorulenSayilar.append(kontrolSayisi)
    print("Tekrar eden sayı yok.")

tekrarKontrol(tekrarEtmeyenSayi)
tekrarKontrol(tekrarEdenSayi)



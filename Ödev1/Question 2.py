import math
toplam = 0
sayilar = []

for i in range(1,101): #Arrayin içini doldurma
    sayilar.append(i)

for x in sayilar:     #Arraydeki sayıları toplama
    toplam += x

print("1-100 arası tüm sayıların toplamı:" + str(toplam))

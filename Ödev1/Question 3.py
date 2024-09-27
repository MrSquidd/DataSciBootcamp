import math
sayilar = []

asalSayi = int(input("Lütfen bir sayı girin:"))

for i in range(2, asalSayi + 1):
    sayilar.append(i)

for i in range(2, int(math.sqrt(asalSayi) + 1)): #The Sieve of Eratosthenes algoritması
    if i in sayilar:
        for j in range(i*i, asalSayi + 1, i):
            if j in sayilar:
                sayilar.remove(j)

    if asalSayi in sayilar:
        print(str(asalSayi) + " asal bir sayı.")
        break
    else:
        print(str(asalSayi) + " asal değil.")
        break








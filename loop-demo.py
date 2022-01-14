

"""
while 0<1:
    for x in range(1,100):
"""       



"""

import random


print("1-100 arası bir sayı tahmin edeceksiniz.")
hak=int(input("Kaç hakkınız olsun:"))
puankaybi=100/hak
puan=100
x=random.randint(1,100)

for a in range(hak):
    cevap=input("Tahmininizi giriniz:")
    if cevap == x:
        break
    else:
        puan=puan-puankaybi

print(f"Puanınız: {puan} ")
print(f"Doğru cevap {x} olmalıydı ")



"""




sayi=int(input("Bir sayı giriniz:"))

if sayi == 1:
    print("1:Asal değildir.")

elif sayi==2:
    print("2:Asal sayıdır.")
for i in range (2, sayi):
    if sayi%i==0:
        
        c="Asal değil"
        break
    else:
        c=("Asaldır")
print(c)
  
        



"""
Daire alanı : pi*r**2
daire cevresi : pi*2*r
yarıçapı verilen bir dare için alan ve çevreyi hesaplayınız
"""
pi=3.14
r= float(input("radius:"))

alan = pi * (r ** 2)
cevre = pi * 2 * r

print("Alan" + str(alan) + " - Çevre:" + str(cevre))
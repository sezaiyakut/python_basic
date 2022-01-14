

# x=1
# while x <= 100:
#     if x%2==1:
#         print(f"{x} tek sayıdır.")
#     else:
#         print(f"{x} çift sayıdır. ")
#     x+=1
# print("bitti")


"""
name=""
while not name:
    name=input("İsminizi giriniz:")
    name=name.strip()
print(f"Merhaba {name}.") 

"""

# sayilar = [1,3,5,7,9,12,19,21]
# x=0
# while x<22:
#     if x in sayilar:
#         print(x)
#         x=x+1
#     else:
#         x=x+1


"""


x=int(input("Başlangıç sayısını giriniz:"))
y=int(input("Bitiş sayısını giriniz:"))
a=0

if x<y:

    while a<=x:
        a+=1


    while x<a<y:
        print(a)
        a=a+1

else:
    while a<=y:
        a+=1
    while y<a<x:
        print(a)
        a+=1
print("bitti")

"""


#iptalll

# x=int(input("Bir sayı giriniz:"))
# y=int(input("Bir sayı giriniz:"))
# z=int(input("Bir sayı giriniz:"))
# t=int(input("Bir sayı giriniz:"))
# u=int(input("Bir sayı giriniz:"))

# liste=[x,y,z,t,u]

# for a in liste:
#     if a>=x and a>=y and a>=z and a>=t and a>=u:
#         print(f"En büyük sayı {a}'dır.")
   
   #iptallll


"""

sayilar=[]
i=0
while i < 5:
    
    sayi=int(input("Bir sayı giriniz"))
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print(sayilar)


"""

ürünsayisi=int(input("Kaç adet ürün gireceksiniz:"))
urunlistesi = []
i=0
while i<ürünsayisi:
    name = input("Ürün adını giriniz:")
    price = input("Ürün fiyatını giriniz:")
    urunlistesi.append( {
        "name" : name,
        "price" : price
    })
    i+=1
print(urunlistesi)

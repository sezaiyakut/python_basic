# sayilar=[1,3,5,7,9,12,19,21]
# for s in sayilar:
#     if s%3==0:
#         print(s)



"""
sayilar=[1,3,5,7,9,12,19,21]
for s in sayilar:
    if s%2==1:
        print(s**2)
"""


# sehirler=["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# for a in sehirler:
#     if len(a)<7:
#         print(a)




urunler=[
    {"name":"samsung S6", "price": "3000"},
    {"name":"samsung S7", "price": "4000"},
    {"name":"samsung S8", "price": "5000"},
    {"name":"samsung S9", "price": "6000"},
    {"name":"samsung S10", "price": "7000"}
]
"""
toplam=0
for urun in urunler:
    toplam+=int(urun["price"])
print(toplam)

"""


for urun in urunler:
    if int(urun["price"]) < 5000:
        print(urun["price"])

"""
class ucus():
    firma = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasire=kapasite
        self.yolcu=yolcu
    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} dakika surecektir.".format(self.kod,self.kalkis,self.varis,self.sure)


ucus1 = ucus("tr011", "ist", "ank", 100, 200, 200)
print(ucus1.varis)
print(ucus1.anons_yap())

"""



# class Ucus():
#     firma = "THY"

#     def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
#         self.kod = kod
#         self.kalkis=kalkis
#         self.varis=varis
#         self.sure=sure
#         self.kapasire=kapasite
#         self.yolcu=yolcu
#     def anons_yap(self):
#             print(f"{self.kod} sefer sayili {self.kalkis}-{self.varis} ucusumuz {self.sure} dakika surecektir.")
        

# ucus1 = Ucus("tr011", "ist", "ank", 100, 200, 200)
# print(ucus1.varis)
# ucus1.anons_yap()


class Ucus():
    firma = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu
    def anons_yap(self):
        print(f"{self.kod} sefer sayili {self.kalkis}-{self.varis} ucusumuz {self.sure} dakika surecektir.")
    def koltuk_guncelle(self):
        
        return self.kapasite - self.yolcu
    def bilet_satis(self, bilet_adedi=1):
        self.yolcu+=bilet_adedi
        self.koltuk_guncelle()
        print("{} adet bilet satılmıştır, kalan koltuk sayisi {} ".format(
            bilet_adedi,
            self.koltuk_guncelle()
        ))
       
        
        
        


ucus1 = Ucus("tr011", "ist", "ank", 100, 400, 100)

ucus1.bilet_satis(5)
